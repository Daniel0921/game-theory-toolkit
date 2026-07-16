"""Dynamic two- or three-firm Cournot competition analyzer."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence, Tuple
import argparse
import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


@dataclass(frozen=True)
class MarketConfig:
    number_of_firms: int
    demand_intercept: float
    demand_slope: float
    marginal_costs: Tuple[float, ...]
    fixed_costs: Tuple[float, ...]
    deviation_size: float = 1.0

    def validate(self) -> None:
        if self.number_of_firms not in (2, 3):
            raise ValueError("The analyzer supports either 2 or 3 firms.")
        if self.demand_slope <= 0:
            raise ValueError("Demand slope b must be greater than zero.")
        if len(self.marginal_costs) != self.number_of_firms:
            raise ValueError("Enter one marginal cost per firm.")
        if len(self.fixed_costs) != self.number_of_firms:
            raise ValueError("Enter one fixed cost per firm.")
        if self.deviation_size <= 0:
            raise ValueError("Deviation size must be greater than zero.")
        values = (
            self.demand_intercept,
            self.demand_slope,
            *self.marginal_costs,
            *self.fixed_costs,
            self.deviation_size,
        )
        if any(not math.isfinite(v) for v in values):
            raise ValueError("All inputs must be finite numbers.")


@dataclass
class SymbolicModel:
    quantities: Tuple[sp.Symbol, ...]
    total_quantity: sp.Expr
    price: sp.Expr
    profits: Tuple[sp.Expr, ...]
    first_derivatives: Tuple[sp.Expr, ...]
    second_derivatives: Tuple[sp.Expr, ...]
    reaction_functions: Tuple[sp.Expr, ...]


@dataclass
class Equilibrium:
    quantities: Tuple[float, ...]
    active_firms: Tuple[int, ...]
    total_quantity: float
    price: float
    variable_profits: Tuple[float, ...]
    accounting_profits: Tuple[float, ...]


def fmt(value: float) -> str:
    if abs(value) < 0.0000001:
        value = 0.0
    return f"{value:,.2f}"


def s_number(value: float) -> sp.Expr:
    return sp.Rational(str(value))


def build_symbolic_model(config: MarketConfig) -> SymbolicModel:
    config.validate()
    q = tuple(sp.symbols(f"q1:{config.number_of_firms + 1}", nonnegative=True))
    a = s_number(config.demand_intercept)
    b = s_number(config.demand_slope)
    total_q = sp.Add(*q)
    price = sp.expand(a - b * total_q)

    profits: List[sp.Expr] = []
    first: List[sp.Expr] = []
    second: List[sp.Expr] = []
    reactions: List[sp.Expr] = []

    for i, qi in enumerate(q):
        c = s_number(config.marginal_costs[i])
        f = s_number(config.fixed_costs[i])
        profit = sp.expand((price - c) * qi - f)
        derivative = sp.expand(sp.diff(profit, qi))
        second_derivative = sp.simplify(sp.diff(derivative, qi))
        solution = sp.solve(sp.Eq(derivative, 0), qi)
        if not solution:
            raise RuntimeError(f"Could not derive Firm {i + 1}'s reaction function.")
        profits.append(profit)
        first.append(derivative)
        second.append(second_derivative)
        reactions.append(sp.simplify(solution[0]))

    return SymbolicModel(
        quantities=q,
        total_quantity=total_q,
        price=price,
        profits=tuple(profits),
        first_derivatives=tuple(first),
        second_derivatives=tuple(second),
        reaction_functions=tuple(reactions),
    )


def solve_active_set(config: MarketConfig, active: Sequence[int]) -> dict[int, float]:
    if not active:
        return {}
    m = len(active)
    matrix = np.ones((m, m), dtype=float)
    np.fill_diagonal(matrix, 2.0)
    rhs = np.array(
        [
            (config.demand_intercept - config.marginal_costs[i])
            / config.demand_slope
            for i in active
        ],
        dtype=float,
    )
    solution = np.linalg.solve(matrix, rhs)
    return {firm: float(solution[pos]) for pos, firm in enumerate(active)}


def best_response(config: MarketConfig, firm: int, quantities: Sequence[float]) -> float:
    rivals = sum(q for i, q in enumerate(quantities) if i != firm)
    numerator = (
        config.demand_intercept
        - config.marginal_costs[firm]
        - config.demand_slope * rivals
    )
    return max(0.0, numerator / (2.0 * config.demand_slope))


def solve_equilibrium(config: MarketConfig) -> Equilibrium:
    """Solve the Cournot game with the non-negativity constraint q_i >= 0."""
    config.validate()
    n = config.number_of_firms
    candidates: list[tuple[tuple[int, ...], tuple[float, ...]]] = []

    for mask in range(1, 1 << n):
        active = tuple(i for i in range(n) if mask & (1 << i))
        proposed = solve_active_set(config, active)
        quantities = [0.0] * n
        for firm, quantity in proposed.items():
            quantities[firm] = quantity

        active_positive = all(quantities[i] > 1e-9 for i in active)
        inactive_satisfied = all(
            best_response(config, i, quantities) <= 1e-8
            for i in range(n)
            if i not in active
        )
        if active_positive and inactive_satisfied:
            candidates.append((active, tuple(quantities)))

    zero = tuple(0.0 for _ in range(n))
    if all(best_response(config, i, zero) <= 1e-8 for i in range(n)):
        candidates.append((tuple(), zero))

    if not candidates:
        raise RuntimeError("No nonnegative Cournot equilibrium could be found.")

    active, quantities = candidates[0]
    total_q = sum(quantities)
    price = config.demand_intercept - config.demand_slope * total_q
    variable = tuple(
        (price - config.marginal_costs[i]) * quantities[i]
        for i in range(n)
    )
    accounting = tuple(variable[i] - config.fixed_costs[i] for i in range(n))

    return Equilibrium(
        quantities=quantities,
        active_firms=active,
        total_quantity=total_q,
        price=price,
        variable_profits=variable,
        accounting_profits=accounting,
    )


def profit_for_choice(
    config: MarketConfig,
    firm: int,
    own_quantity: float,
    equilibrium_quantities: Sequence[float],
) -> float:
    rivals = sum(q for i, q in enumerate(equilibrium_quantities) if i != firm)
    price = config.demand_intercept - config.demand_slope * (own_quantity + rivals)
    return (
        (price - config.marginal_costs[firm]) * own_quantity
        - config.fixed_costs[firm]
    )


def monopoly_benchmark(config: MarketConfig) -> tuple[float, float, float]:
    c = min(config.marginal_costs)
    q = max(0.0, (config.demand_intercept - c) / (2 * config.demand_slope))
    p = config.demand_intercept - config.demand_slope * q
    profit = (p - c) * q
    return q, p, profit


def competitive_benchmark(config: MarketConfig) -> tuple[float, float]:
    c = min(config.marginal_costs)
    q = max(0.0, (config.demand_intercept - c) / config.demand_slope)
    p = config.demand_intercept - config.demand_slope * q
    return q, p


def create_plots(config: MarketConfig, equilibrium: Equilibrium, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    a, b = config.demand_intercept, config.demand_slope
    max_q = max((a - min(config.marginal_costs)) / b, 1.0)
    grid = np.linspace(0, max_q, 400)

    if config.number_of_firms == 2:
        r1 = np.maximum(0, (a - config.marginal_costs[0] - b * grid) / (2 * b))
        r2 = np.maximum(0, (a - config.marginal_costs[1] - b * grid) / (2 * b))
        fig, ax = plt.subplots(figsize=(9, 7))
        ax.plot(grid, r1, label="Firm 1 reaction")
        ax.plot(r2, grid, label="Firm 2 reaction")
        ax.scatter(equilibrium.quantities[1], equilibrium.quantities[0], s=80, label="Nash equilibrium")
        ax.set_xlabel("Firm 2 quantity")
        ax.set_ylabel("Firm 1 quantity")
        ax.set_title("Cournot Reaction Functions")
        ax.grid(True)
        ax.legend()
        fig.tight_layout()
        fig.savefig(output_dir / "reaction_functions.png", dpi=180)
        plt.close(fig)
        return

    pairs = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
    for first, second, fixed in pairs:
        fixed_q = equilibrium.quantities[fixed]
        first_response = np.maximum(
            0,
            (a - config.marginal_costs[first] - b * grid - b * fixed_q) / (2 * b),
        )
        second_response = np.maximum(
            0,
            (a - config.marginal_costs[second] - b * grid - b * fixed_q) / (2 * b),
        )
        fig, ax = plt.subplots(figsize=(9, 7))
        ax.plot(grid, first_response, label=f"Firm {first + 1} reaction")
        ax.plot(second_response, grid, label=f"Firm {second + 1} reaction")
        ax.scatter(
            equilibrium.quantities[second],
            equilibrium.quantities[first],
            s=80,
            label="Conditional equilibrium",
        )
        ax.set_xlabel(f"Firm {second + 1} quantity")
        ax.set_ylabel(f"Firm {first + 1} quantity")
        ax.set_title(
            f"Firms {first + 1} and {second + 1}: "
            f"Firm {fixed + 1} fixed at {fixed_q:.2f}"
        )
        ax.grid(True)
        ax.legend()
        fig.tight_layout()
        filename = (
            f"reaction_functions_firms_{first + 1}_{second + 1}_"
            f"holding_firm_{fixed + 1}_fixed.png"
        )
        fig.savefig(output_dir / filename, dpi=180)
        plt.close(fig)


def generate_report(
    config: MarketConfig,
    model: SymbolicModel,
    equilibrium: Equilibrium,
    output_dir: Path,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    report = output_dir / "Example_Output.md"
    lines: List[str] = []

    lines += [
        "# Cournot Competition Analyzer — Example Output",
        "",
        "This report was generated automatically by `cournot_competition_analyzer.py`.",
        "",
        "## 1. Market Configuration",
        "",
        f"- Firms: **{config.number_of_firms}**",
        f"- Inverse demand: **P(Q) = {fmt(config.demand_intercept)} - {fmt(config.demand_slope)}Q**",
        f"- Marginal costs: **{', '.join(fmt(c) for c in config.marginal_costs)}**",
        f"- Fixed costs: **{', '.join(fmt(f) for f in config.fixed_costs)}**",
        "",
        "Total output is the sum of all firms' quantities:",
        "",
        "$$",
        "Q = " + " + ".join(f"q_{i + 1}" for i in range(config.number_of_firms)),
        "$$",
        "",
        "## 2. Profit Functions",
        "",
    ]

    for i, profit in enumerate(model.profits):
        lines += [
            f"### Firm {i + 1}",
            "",
            "$$",
            rf"\pi_{i + 1} = {sp.latex(profit)}",
            "$$",
            "",
            (
                f"Firm {i + 1} earns revenue from its own quantity, but every "
                "firm's output lowers the common market price. Fixed cost affects "
                "accounting profit but does not alter the reaction function."
            ),
            "",
        ]

    lines += [
        "## 3. Calculus and Reaction Functions",
        "",
        (
            "Each firm treats rival quantities as fixed, differentiates its profit "
            "with respect to its own quantity, and sets the derivative equal to zero."
        ),
        "",
    ]

    for i in range(config.number_of_firms):
        lines += [
            f"### Firm {i + 1}",
            "",
            "First derivative:",
            "",
            "$$",
            rf"\frac{{\partial \pi_{i + 1}}}{{\partial q_{i + 1}}} = {sp.latex(model.first_derivatives[i])}",
            "$$",
            "",
            "Reaction function:",
            "",
            "$$",
            rf"q_{i + 1} = {sp.latex(model.reaction_functions[i])}",
            "$$",
            "",
            "Second derivative:",
            "",
            "$$",
            rf"\frac{{\partial^2 \pi_{i + 1}}}{{\partial q_{i + 1}^2}} = {sp.latex(model.second_derivatives[i])}",
            "$$",
            "",
            (
                "The second derivative is negative because the demand slope is positive. "
                "Therefore, the first-order condition identifies a profit maximum."
            ),
            "",
        ]

    lines += [
        "## 4. Cournot-Nash Equilibrium",
        "",
        "| Firm | Quantity | Marginal cost | Fixed cost | Variable profit | Accounting profit |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for i in range(config.number_of_firms):
        lines.append(
            f"| Firm {i + 1} | {fmt(equilibrium.quantities[i])} | "
            f"{fmt(config.marginal_costs[i])} | {fmt(config.fixed_costs[i])} | "
            f"{fmt(equilibrium.variable_profits[i])} | {fmt(equilibrium.accounting_profits[i])} |"
        )

    lines += [
        "",
        f"- Total market output: **{fmt(equilibrium.total_quantity)}**",
        f"- Market price: **{fmt(equilibrium.price)}**",
        f"- Total accounting profit: **{fmt(sum(equilibrium.accounting_profits))}**",
        "",
        "## 5. Best-Response Verification",
        "",
        "| Firm | Equilibrium quantity | Calculated best response | Verified? |",
        "|---:|---:|---:|:---:|",
    ]

    for i, quantity in enumerate(equilibrium.quantities):
        response = best_response(config, i, equilibrium.quantities)
        verified = abs(quantity - response) <= 1e-7
        lines.append(
            f"| Firm {i + 1} | {fmt(quantity)} | {fmt(response)} | {'Yes' if verified else 'No'} |"
        )

    lines += [
        "",
        (
            "Every firm is choosing its profit-maximizing quantity given its rivals' "
            "quantities. No firm can improve by changing output alone, so the solution "
            "is a Cournot-Nash equilibrium."
        ),
        "",
        "## 6. Unilateral Deviation Tests",
        "",
        f"Each firm is tested at **±{fmt(config.deviation_size)} unit(s)** from equilibrium.",
        "",
        "| Firm | Equilibrium q | Equilibrium profit | Lower q | Lower-q profit | Higher q | Higher-q profit |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for i, q_star in enumerate(equilibrium.quantities):
        lower_q = max(0.0, q_star - config.deviation_size)
        higher_q = q_star + config.deviation_size
        lower_profit = profit_for_choice(config, i, lower_q, equilibrium.quantities)
        higher_profit = profit_for_choice(config, i, higher_q, equilibrium.quantities)
        lines.append(
            f"| Firm {i + 1} | {fmt(q_star)} | {fmt(equilibrium.accounting_profits[i])} | "
            f"{fmt(lower_q)} | {fmt(lower_profit)} | {fmt(higher_q)} | {fmt(higher_profit)} |"
        )

    monopoly_q, monopoly_p, monopoly_profit = monopoly_benchmark(config)
    competitive_q, competitive_p = competitive_benchmark(config)
    lines += [
        "",
        "## 7. Market-Structure Comparison",
        "",
        "| Structure | Total output | Price | Meaning |",
        "|---|---:|---:|---|",
        f"| Joint-profit/monopoly benchmark | {fmt(monopoly_q)} | {fmt(monopoly_p)} | Output chosen to maximize joint variable profit using the lowest-cost technology. |",
        f"| Cournot competition | {fmt(equilibrium.total_quantity)} | {fmt(equilibrium.price)} | Firms choose output strategically and independently. |",
        f"| Perfect-competition benchmark | {fmt(competitive_q)} | {fmt(competitive_p)} | Price is pushed to the lowest constant marginal cost in this simplified benchmark. |",
        "",
        "## 8. Economic Interpretation",
        "",
        (
            "A Cournot firm faces a tradeoff. Producing more creates additional sales, "
            "but it also increases total market output and lowers the market price on "
            "every unit the firm sells. The reaction function gives the quantity that "
            "best balances those effects for each possible level of rival output."
        ),
        "",
        (
            "At equilibrium, all reaction functions are satisfied simultaneously. "
            "The outcome is stable against unilateral deviations even though a coordinated "
            "industry might prefer the lower-output monopoly benchmark."
        ),
        "",
        "## 9. Visualizations",
        "",
    ]

    if config.number_of_firms == 2:
        lines.append("![Reaction functions](./reaction_functions.png)")
    else:
        lines += [
            (
                "With three firms, the reaction functions occupy three-dimensional strategy "
                "space. These charts show pairwise conditional reaction functions while "
                "holding the third firm at its equilibrium quantity."
            ),
            "",
            "![Firms 1 and 2](./reaction_functions_firms_1_2_holding_firm_3_fixed.png)",
            "",
            "![Firms 1 and 3](./reaction_functions_firms_1_3_holding_firm_2_fixed.png)",
            "",
            "![Firms 2 and 3](./reaction_functions_firms_2_3_holding_firm_1_fixed.png)",
        ]

    report.write_text("\n".join(lines), encoding="utf-8")
    return report


def print_summary(config: MarketConfig, model: SymbolicModel, equilibrium: Equilibrium) -> None:
    print("=" * 78)
    print("COURNOT COMPETITION ANALYZER")
    print("=" * 78)
    print(f"Inverse demand: P = {config.demand_intercept:g} - {config.demand_slope:g}Q")
    print(f"Firms: {config.number_of_firms}\n")

    for i in range(config.number_of_firms):
        print(f"FIRM {i + 1}")
        print("Profit function:")
        sp.pprint(model.profits[i])
        print("First derivative:")
        sp.pprint(model.first_derivatives[i])
        print("Reaction function:")
        sp.pprint(sp.Eq(model.quantities[i], model.reaction_functions[i]))
        print("Second derivative:")
        sp.pprint(model.second_derivatives[i])
        print("-" * 78)

    print("COURNOT-NASH EQUILIBRIUM")
    print("-" * 78)
    for i, q in enumerate(equilibrium.quantities):
        print(
            f"Firm {i + 1}: quantity = {fmt(q)}, "
            f"accounting profit = {fmt(equilibrium.accounting_profits[i])}"
        )
    print(f"Total output: {fmt(equilibrium.total_quantity)}")
    print(f"Market price: {fmt(equilibrium.price)}")
    print("\nNash explanation:")
    print(
        "Every firm is choosing its best response to the other firms' quantities. "
        "No firm can increase profit by changing output alone."
    )


def prompt_float(label: str, default: float) -> float:
    raw = input(f"{label} [{default}]: ").strip()
    return default if raw == "" else float(raw)


def interactive_config() -> MarketConfig:
    print("Press Enter to accept each default.\n")
    raw_n = input("Number of firms (2 or 3) [3]: ").strip()
    n = 3 if raw_n == "" else int(raw_n)
    a = prompt_float("Demand intercept a", 100.0)
    b = prompt_float("Demand slope b", 1.0)
    marginal_costs = []
    fixed_costs = []
    for i in range(n):
        marginal_costs.append(prompt_float(f"Firm {i + 1} marginal cost", 20.0))
        fixed_costs.append(prompt_float(f"Firm {i + 1} fixed cost", 0.0))
    deviation = prompt_float("Deviation-test size", 1.0)
    config = MarketConfig(n, a, b, tuple(marginal_costs), tuple(fixed_costs), deviation)
    config.validate()
    return config


def default_config() -> MarketConfig:
    return MarketConfig(
        number_of_firms=3,
        demand_intercept=100.0,
        demand_slope=1.0,
        marginal_costs=(20.0, 20.0, 20.0),
        fixed_costs=(0.0, 0.0, 0.0),
        deviation_size=1.0,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Two- or three-firm Cournot analyzer")
    parser.add_argument("--interactive", action="store_true", help="Enter custom market inputs")
    parser.add_argument("--output-dir", default="output", help="Folder for generated report and charts")
    args = parser.parse_args()

    config = interactive_config() if args.interactive else default_config()
    model = build_symbolic_model(config)
    equilibrium = solve_equilibrium(config)
    output_dir = Path(args.output_dir)

    print_summary(config, model, equilibrium)
    report = generate_report(config, model, equilibrium, output_dir)
    create_plots(config, equilibrium, output_dir)

    print("\nGenerated files:")
    print(f"- {report}")
    for image in sorted(output_dir.glob("*.png")):
        print(f"- {image}")


if __name__ == "__main__":
    main()
