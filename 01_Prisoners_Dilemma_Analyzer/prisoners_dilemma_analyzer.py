# Prisoner's Dilemma: Detailed Oligopoly Analyzer
#
# This script:
# 1. Displays the payoff matrix
# 2. Explains every possible outcome
# 3. Compares how each outcome affects Firm 1 and Firm 2
# 4. Identifies each firm's best responses
# 5. Identifies dominant strategies
# 6. Finds pure-strategy Nash equilibria
# 7. Explains why the Nash equilibrium occurs
# 8. Compares the Nash equilibrium with the cooperative outcome

from typing import Dict, List, Optional, Tuple


Strategy = str
Payoff = Tuple[float, float]
Outcome = Tuple[Strategy, Strategy]


# ============================================================
# GAME SETTINGS
# ============================================================

FIRM_1_STRATEGIES = ["Low output", "High output"]
FIRM_2_STRATEGIES = ["Low output", "High output"]

# Payoffs are listed as:
# (Firm 1 strategy, Firm 2 strategy): (Firm 1 payoff, Firm 2 payoff)

PAYOFF_MATRIX: Dict[Outcome, Payoff] = {
    ("Low output", "Low output"): (3, 3),
    ("Low output", "High output"): (0, 5),
    ("High output", "Low output"): (5, 0),
    ("High output", "High output"): (2, 2),
}


# ============================================================
# VALIDATION
# ============================================================

def validate_payoff_matrix(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> None:
    """
    Confirms that every possible strategy combination has a payoff.
    """

    expected_outcomes = {
        (firm1_strategy, firm2_strategy)
        for firm1_strategy in firm1_strategies
        for firm2_strategy in firm2_strategies
    }

    missing_outcomes = expected_outcomes - set(payoff_matrix.keys())

    if missing_outcomes:
        raise ValueError(
            "The payoff matrix is missing these outcomes: "
            f"{sorted(missing_outcomes)}"
        )

    for outcome, payoff in payoff_matrix.items():
        if len(payoff) != 2:
            raise ValueError(
                f"The payoff for {outcome} must contain exactly "
                "two numbers."
            )


# ============================================================
# FORMATTING FUNCTIONS
# ============================================================

def format_number(value: float) -> str:
    """
    Formats whole numbers without decimal places.
    """

    if float(value).is_integer():
        return str(int(value))

    return f"{value:.2f}"


def strategy_description(strategy: Strategy) -> str:
    """
    Converts a strategy name into an economic description.
    """

    lower_strategy = strategy.lower()

    if "low output" in lower_strategy:
        return (
            "restrict production, helping maintain a higher market price"
        )

    if "high output" in lower_strategy:
        return (
            "increase production, which tends to push the market price lower"
        )

    return f"choose the strategy '{strategy}'"


def print_section(title: str) -> None:
    """
    Prints a formatted section heading.
    """

    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ============================================================
# PAYOFF MATRIX DISPLAY
# ============================================================

def display_payoff_matrix(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> None:
    """
    Displays the payoff matrix in a readable table.
    """

    print_section("PAYOFF MATRIX")

    print(
        "Each cell is shown as "
        "(Firm 1 payoff, Firm 2 payoff).\n"
    )

    first_column_width = 24
    cell_width = 26

    header = f"{'Firm 1 / Firm 2':<{first_column_width}}"

    for firm2_strategy in firm2_strategies:
        header += f"{firm2_strategy:^{cell_width}}"

    print(header)
    print("-" * len(header))

    for firm1_strategy in firm1_strategies:
        row = f"{firm1_strategy:<{first_column_width}}"

        for firm2_strategy in firm2_strategies:
            payoff = payoff_matrix[
                (firm1_strategy, firm2_strategy)
            ]

            payoff_text = (
                f"({format_number(payoff[0])}, "
                f"{format_number(payoff[1])})"
            )

            row += f"{payoff_text:^{cell_width}}"

        print(row)


# ============================================================
# BEST RESPONSES
# ============================================================

def get_best_responses_for_firm1(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> Dict[Strategy, List[Strategy]]:
    """
    Finds Firm 1's best response to each Firm 2 strategy.
    """

    best_responses: Dict[Strategy, List[Strategy]] = {}

    for firm2_strategy in firm2_strategies:
        available_payoffs = {
            firm1_strategy:
                payoff_matrix[
                    (firm1_strategy, firm2_strategy)
                ][0]
            for firm1_strategy in firm1_strategies
        }

        highest_payoff = max(available_payoffs.values())

        best_responses[firm2_strategy] = [
            strategy
            for strategy, payoff in available_payoffs.items()
            if payoff == highest_payoff
        ]

    return best_responses


def get_best_responses_for_firm2(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> Dict[Strategy, List[Strategy]]:
    """
    Finds Firm 2's best response to each Firm 1 strategy.
    """

    best_responses: Dict[Strategy, List[Strategy]] = {}

    for firm1_strategy in firm1_strategies:
        available_payoffs = {
            firm2_strategy:
                payoff_matrix[
                    (firm1_strategy, firm2_strategy)
                ][1]
            for firm2_strategy in firm2_strategies
        }

        highest_payoff = max(available_payoffs.values())

        best_responses[firm1_strategy] = [
            strategy
            for strategy, payoff in available_payoffs.items()
            if payoff == highest_payoff
        ]

    return best_responses


# ============================================================
# DOMINANT STRATEGIES
# ============================================================

def find_strictly_dominant_strategy_firm1(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> Optional[Strategy]:
    """
    Finds Firm 1's strictly dominant strategy, if one exists.
    """

    for candidate in firm1_strategies:
        candidate_is_dominant = True

        for firm2_strategy in firm2_strategies:
            candidate_payoff = payoff_matrix[
                (candidate, firm2_strategy)
            ][0]

            for alternative in firm1_strategies:
                if alternative == candidate:
                    continue

                alternative_payoff = payoff_matrix[
                    (alternative, firm2_strategy)
                ][0]

                if candidate_payoff <= alternative_payoff:
                    candidate_is_dominant = False
                    break

            if not candidate_is_dominant:
                break

        if candidate_is_dominant:
            return candidate

    return None


def find_strictly_dominant_strategy_firm2(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> Optional[Strategy]:
    """
    Finds Firm 2's strictly dominant strategy, if one exists.
    """

    for candidate in firm2_strategies:
        candidate_is_dominant = True

        for firm1_strategy in firm1_strategies:
            candidate_payoff = payoff_matrix[
                (firm1_strategy, candidate)
            ][1]

            for alternative in firm2_strategies:
                if alternative == candidate:
                    continue

                alternative_payoff = payoff_matrix[
                    (firm1_strategy, alternative)
                ][1]

                if candidate_payoff <= alternative_payoff:
                    candidate_is_dominant = False
                    break

            if not candidate_is_dominant:
                break

        if candidate_is_dominant:
            return candidate

    return None


# ============================================================
# NASH EQUILIBRIUM
# ============================================================

def find_nash_equilibria(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> List[Outcome]:
    """
    Finds all pure-strategy Nash equilibria.
    """

    firm1_best_responses = get_best_responses_for_firm1(
        payoff_matrix,
        firm1_strategies,
        firm2_strategies,
    )

    firm2_best_responses = get_best_responses_for_firm2(
        payoff_matrix,
        firm1_strategies,
        firm2_strategies,
    )

    equilibria: List[Outcome] = []

    for firm1_strategy in firm1_strategies:
        for firm2_strategy in firm2_strategies:
            firm1_is_best_responding = (
                firm1_strategy
                in firm1_best_responses[firm2_strategy]
            )

            firm2_is_best_responding = (
                firm2_strategy
                in firm2_best_responses[firm1_strategy]
            )

            if firm1_is_best_responding and firm2_is_best_responding:
                equilibria.append(
                    (firm1_strategy, firm2_strategy)
                )

    return equilibria


# ============================================================
# JOINT PAYOFF
# ============================================================

def find_joint_profit_maximum(
    payoff_matrix: Dict[Outcome, Payoff],
) -> Tuple[List[Outcome], float]:
    """
    Finds the outcome with the greatest combined payoff.
    """

    combined_payoffs = {
        outcome: payoff[0] + payoff[1]
        for outcome, payoff in payoff_matrix.items()
    }

    highest_combined_payoff = max(combined_payoffs.values())

    best_outcomes = [
        outcome
        for outcome, combined_payoff
        in combined_payoffs.items()
        if combined_payoff == highest_combined_payoff
    ]

    return best_outcomes, highest_combined_payoff


# ============================================================
# SCENARIO EXPLANATIONS
# ============================================================

def explain_unilateral_changes(
    payoff_matrix: Dict[Outcome, Payoff],
    current_outcome: Outcome,
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> None:
    """
    Explains what happens if either firm changes strategy alone.
    """

    firm1_strategy, firm2_strategy = current_outcome
    current_payoff = payoff_matrix[current_outcome]

    print("\nUnilateral decision analysis:")

    for alternative_firm1_strategy in firm1_strategies:
        if alternative_firm1_strategy == firm1_strategy:
            continue

        alternative_outcome = (
            alternative_firm1_strategy,
            firm2_strategy,
        )

        alternative_payoff = payoff_matrix[
            alternative_outcome
        ][0]

        payoff_change = alternative_payoff - current_payoff[0]

        if payoff_change > 0:
            print(
                f"  • Firm 1 could increase its payoff from "
                f"{format_number(current_payoff[0])} to "
                f"{format_number(alternative_payoff)} by changing "
                f"alone from '{firm1_strategy}' to "
                f"'{alternative_firm1_strategy}'."
            )
        elif payoff_change < 0:
            print(
                f"  • Firm 1 would reduce its payoff from "
                f"{format_number(current_payoff[0])} to "
                f"{format_number(alternative_payoff)} by changing "
                f"alone from '{firm1_strategy}' to "
                f"'{alternative_firm1_strategy}'."
            )
        else:
            print(
                f"  • Firm 1 would receive the same payoff by "
                f"changing alone to "
                f"'{alternative_firm1_strategy}'."
            )

    for alternative_firm2_strategy in firm2_strategies:
        if alternative_firm2_strategy == firm2_strategy:
            continue

        alternative_outcome = (
            firm1_strategy,
            alternative_firm2_strategy,
        )

        alternative_payoff = payoff_matrix[
            alternative_outcome
        ][1]

        payoff_change = alternative_payoff - current_payoff[1]

        if payoff_change > 0:
            print(
                f"  • Firm 2 could increase its payoff from "
                f"{format_number(current_payoff[1])} to "
                f"{format_number(alternative_payoff)} by changing "
                f"alone from '{firm2_strategy}' to "
                f"'{alternative_firm2_strategy}'."
            )
        elif payoff_change < 0:
            print(
                f"  • Firm 2 would reduce its payoff from "
                f"{format_number(current_payoff[1])} to "
                f"{format_number(alternative_payoff)} by changing "
                f"alone from '{firm2_strategy}' to "
                f"'{alternative_firm2_strategy}'."
            )
        else:
            print(
                f"  • Firm 2 would receive the same payoff by "
                f"changing alone to "
                f"'{alternative_firm2_strategy}'."
            )


def explain_scenario(
    payoff_matrix: Dict[Outcome, Payoff],
    outcome: Outcome,
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
    scenario_number: int,
) -> None:
    """
    Provides a detailed explanation of one strategy combination.
    """

    firm1_strategy, firm2_strategy = outcome
    firm1_payoff, firm2_payoff = payoff_matrix[outcome]

    combined_payoff = firm1_payoff + firm2_payoff

    print_section(
        f"SCENARIO {scenario_number}: "
        f"FIRM 1 CHOOSES '{firm1_strategy.upper()}' AND "
        f"FIRM 2 CHOOSES '{firm2_strategy.upper()}'"
    )

    print(
        f"Firm 1 chooses to "
        f"{strategy_description(firm1_strategy)}."
    )

    print(
        f"Firm 2 chooses to "
        f"{strategy_description(firm2_strategy)}."
    )

    print(
        f"\nThe resulting payoff is "
        f"({format_number(firm1_payoff)}, "
        f"{format_number(firm2_payoff)})."
    )

    print(
        f"Firm 1 receives {format_number(firm1_payoff)}, "
        f"Firm 2 receives {format_number(firm2_payoff)}, "
        f"and the firms' combined payoff is "
        f"{format_number(combined_payoff)}."
    )

    # Scenario-specific economic explanation
    if (
        firm1_strategy == "Low output"
        and firm2_strategy == "Low output"
    ):
        print(
            "\nEconomic interpretation:"
        )

        print(
            "Both firms limit production. Because total market "
            "output remains relatively low, the market price stays "
            "relatively high."
        )

        print(
            "This benefits both firms because neither one floods the "
            "market with additional output. Each firm earns a payoff "
            "of 3."
        )

        print(
            "This is the cooperative or joint-profit outcome. The "
            "firms collectively earn 6, which is greater than the "
            "combined payoff of 4 when both choose high output."
        )

        print(
            "However, the outcome is unstable. Each firm can earn 5 "
            "instead of 3 by secretly increasing its own output while "
            "the other firm continues restricting production."
        )

    elif (
        firm1_strategy == "Low output"
        and firm2_strategy == "High output"
    ):
        print(
            "\nEconomic interpretation:"
        )

        print(
            "Firm 1 restricts production, but Firm 2 expands "
            "production."
        )

        print(
            "Firm 2 captures a larger share of the market while "
            "taking advantage of the fact that Firm 1 has kept its "
            "own output low."
        )

        print(
            f"Firm 2 receives the highest individual payoff of "
            f"{format_number(firm2_payoff)}."
        )

        print(
            f"Firm 1 is harmed and receives only "
            f"{format_number(firm1_payoff)} because it restricts "
            "output while its rival aggressively produces more."
        )

        print(
            "Firm 1 would not willingly remain in this position. It "
            "has a strong incentive to increase output in response."
        )

    elif (
        firm1_strategy == "High output"
        and firm2_strategy == "Low output"
    ):
        print(
            "\nEconomic interpretation:"
        )

        print(
            "Firm 1 expands production while Firm 2 restricts "
            "production."
        )

        print(
            "Firm 1 captures the advantage from producing more while "
            "Firm 2 helps maintain a relatively favorable market "
            "price by keeping its own output low."
        )

        print(
            f"Firm 1 receives the highest individual payoff of "
            f"{format_number(firm1_payoff)}."
        )

        print(
            f"Firm 2 is harmed and receives only "
            f"{format_number(firm2_payoff)} because it produces less "
            "while Firm 1 takes additional market share."
        )

        print(
            "Firm 2 therefore has a strong incentive to respond by "
            "increasing its own output."
        )

    elif (
        firm1_strategy == "High output"
        and firm2_strategy == "High output"
    ):
        print(
            "\nEconomic interpretation:"
        )

        print(
            "Both firms expand production. Total market output rises, "
            "which places downward pressure on the market price."
        )

        print(
            "Neither firm allows the other to gain the advantage from "
            "being the only high-output producer."
        )

        print(
            f"Each firm receives a payoff of "
            f"{format_number(firm1_payoff)}."
        )

        print(
            "Both firms are worse off than they would be if they both "
            "restricted output. Under mutual low output, each would "
            "receive 3 instead of 2."
        )

        print(
            "Even so, neither firm can improve its payoff by reducing "
            "output alone. If one firm reduces output while the other "
            "continues producing at a high level, the firm that "
            "reduces output falls from 2 to 0."
        )

    else:
        print(
            "\nEconomic interpretation:"
        )

        print(
            "The firms' strategy choices determine how the market "
            "benefits are divided between them."
        )

    explain_unilateral_changes(
        payoff_matrix,
        outcome,
        firm1_strategies,
        firm2_strategies,
    )


def explain_all_scenarios(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> None:
    """
    Explains every possible strategy combination.
    """

    scenario_number = 1

    for firm1_strategy in firm1_strategies:
        for firm2_strategy in firm2_strategies:
            explain_scenario(
                payoff_matrix,
                (firm1_strategy, firm2_strategy),
                firm1_strategies,
                firm2_strategies,
                scenario_number,
            )

            scenario_number += 1


# ============================================================
# BEST-RESPONSE EXPLANATIONS
# ============================================================

def explain_best_responses(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> None:
    """
    Explains each firm's best response to the other firm's choice.
    """

    print_section("BEST-RESPONSE ANALYSIS")

    print("Firm 1's decisions:")

    for firm2_strategy in firm2_strategies:
        print(
            f"\nIf Firm 2 chooses '{firm2_strategy}':"
        )

        firm1_options = []

        for firm1_strategy in firm1_strategies:
            payoff = payoff_matrix[
                (firm1_strategy, firm2_strategy)
            ][0]

            firm1_options.append(
                (firm1_strategy, payoff)
            )

            print(
                f"  • If Firm 1 chooses '{firm1_strategy}', "
                f"Firm 1 receives {format_number(payoff)}."
            )

        best_payoff = max(
            payoff for _, payoff in firm1_options
        )

        best_choices = [
            strategy
            for strategy, payoff in firm1_options
            if payoff == best_payoff
        ]

        print(
            f"  Therefore, Firm 1's best response is: "
            f"{', '.join(best_choices)}."
        )

    print("\nFirm 2's decisions:")

    for firm1_strategy in firm1_strategies:
        print(
            f"\nIf Firm 1 chooses '{firm1_strategy}':"
        )

        firm2_options = []

        for firm2_strategy in firm2_strategies:
            payoff = payoff_matrix[
                (firm1_strategy, firm2_strategy)
            ][1]

            firm2_options.append(
                (firm2_strategy, payoff)
            )

            print(
                f"  • If Firm 2 chooses '{firm2_strategy}', "
                f"Firm 2 receives {format_number(payoff)}."
            )

        best_payoff = max(
            payoff for _, payoff in firm2_options
        )

        best_choices = [
            strategy
            for strategy, payoff in firm2_options
            if payoff == best_payoff
        ]

        print(
            f"  Therefore, Firm 2's best response is: "
            f"{', '.join(best_choices)}."
        )


# ============================================================
# NASH EQUILIBRIUM EXPLANATION
# ============================================================

def explain_nash_equilibrium(
    payoff_matrix: Dict[Outcome, Payoff],
    equilibria: List[Outcome],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> None:
    """
    Provides a detailed explanation of every Nash equilibrium.
    """

    print_section("NASH EQUILIBRIUM ANALYSIS")

    if not equilibria:
        print(
            "No pure-strategy Nash equilibrium exists in this game."
        )
        return

    for equilibrium in equilibria:
        firm1_strategy, firm2_strategy = equilibrium
        firm1_payoff, firm2_payoff = payoff_matrix[equilibrium]

        print(
            f"The Nash equilibrium is:\n"
            f"  Firm 1: {firm1_strategy}\n"
            f"  Firm 2: {firm2_strategy}\n"
            f"  Payoffs: "
            f"({format_number(firm1_payoff)}, "
            f"{format_number(firm2_payoff)})"
        )

        print(
            "\nA Nash equilibrium is an outcome where neither firm "
            "can improve its own payoff by changing its strategy "
            "alone while the other firm's strategy stays fixed."
        )

        print("\nFirm 1's incentive at the equilibrium:")

        for alternative in firm1_strategies:
            if alternative == firm1_strategy:
                continue

            alternative_payoff = payoff_matrix[
                (alternative, firm2_strategy)
            ][0]

            print(
                f"  If Firm 1 changes from '{firm1_strategy}' to "
                f"'{alternative}' while Firm 2 remains at "
                f"'{firm2_strategy}', Firm 1's payoff changes from "
                f"{format_number(firm1_payoff)} to "
                f"{format_number(alternative_payoff)}."
            )

        print("\nFirm 2's incentive at the equilibrium:")

        for alternative in firm2_strategies:
            if alternative == firm2_strategy:
                continue

            alternative_payoff = payoff_matrix[
                (firm1_strategy, alternative)
            ][1]

            print(
                f"  If Firm 2 changes from '{firm2_strategy}' to "
                f"'{alternative}' while Firm 1 remains at "
                f"'{firm1_strategy}', Firm 2's payoff changes from "
                f"{format_number(firm2_payoff)} to "
                f"{format_number(alternative_payoff)}."
            )

        print(
            "\nTherefore, neither firm wants to move away from this "
            "outcome on its own."
        )

        print(
            "Firm 1 would be harmed by changing alone, and Firm 2 "
            "would also be harmed by changing alone. The strategies "
            "are therefore mutually stable."
        )


# ============================================================
# PRISONER'S DILEMMA EXPLANATION
# ============================================================

def explain_prisoners_dilemma(
    payoff_matrix: Dict[Outcome, Payoff],
    equilibria: List[Outcome],
    joint_best_outcomes: List[Outcome],
    highest_combined_payoff: float,
) -> None:
    """
    Explains whether the game has the structure of a prisoner's dilemma.
    """

    print_section("WHY THIS IS A PRISONER'S DILEMMA")

    if not equilibria:
        print(
            "The game does not have a pure-strategy Nash equilibrium, "
            "so it does not match the standard prisoner's dilemma "
            "structure."
        )
        return

    equilibrium = equilibria[0]
    equilibrium_payoff = payoff_matrix[equilibrium]
    equilibrium_total = sum(equilibrium_payoff)

    print(
        f"The Nash equilibrium produces payoffs "
        f"({format_number(equilibrium_payoff[0])}, "
        f"{format_number(equilibrium_payoff[1])}), "
        f"for a combined payoff of "
        f"{format_number(equilibrium_total)}."
    )

    print("\nThe maximum combined payoff occurs at:")

    for outcome in joint_best_outcomes:
        payoff = payoff_matrix[outcome]

        print(
            f"  Firm 1 chooses '{outcome[0]}' and "
            f"Firm 2 chooses '{outcome[1]}'."
        )

        print(
            f"  The payoffs are "
            f"({format_number(payoff[0])}, "
            f"{format_number(payoff[1])}), "
            f"for a combined payoff of "
            f"{format_number(highest_combined_payoff)}."
        )

    if equilibrium_total < highest_combined_payoff:
        print(
            "\nThe firms would collectively be better off at the "
            "joint-profit-maximizing outcome."
        )

        print(
            "However, that cooperative outcome is difficult to "
            "maintain because each firm can improve its individual "
            "payoff by increasing output while the other firm keeps "
            "output low."
        )

        print(
            "Because both firms recognize this incentive, both choose "
            "high output."
        )

        print(
            "The result is individually rational but collectively "
            "inferior: each firm protects itself from exploitation, "
            "yet both firms receive less profit than they could have "
            "earned through cooperation."
        )

        print(
            "\nThis conflict between individual incentives and joint "
            "well-being is the defining feature of the prisoner's "
            "dilemma."
        )
    else:
        print(
            "\nThe Nash equilibrium also maximizes the combined "
            "payoff. Therefore, this game is not a standard "
            "prisoner's dilemma."
        )


# ============================================================
# FINAL SUMMARY
# ============================================================

def print_final_summary(
    payoff_matrix: Dict[Outcome, Payoff],
    dominant_firm1: Optional[Strategy],
    dominant_firm2: Optional[Strategy],
    equilibria: List[Outcome],
) -> None:
    """
    Prints the main findings in a condensed format.
    """

    print_section("FINAL SUMMARY")

    if dominant_firm1:
        print(
            f"Firm 1's strictly dominant strategy is "
            f"'{dominant_firm1}'."
        )
    else:
        print(
            "Firm 1 does not have a strictly dominant strategy."
        )

    if dominant_firm2:
        print(
            f"Firm 2's strictly dominant strategy is "
            f"'{dominant_firm2}'."
        )
    else:
        print(
            "Firm 2 does not have a strictly dominant strategy."
        )

    if equilibria:
        print("\nPure-strategy Nash equilibrium:")

        for equilibrium in equilibria:
            payoff = payoff_matrix[equilibrium]

            print(
                f"  Firm 1 chooses '{equilibrium[0]}', "
                f"Firm 2 chooses '{equilibrium[1]}', "
                f"and the payoffs are "
                f"({format_number(payoff[0])}, "
                f"{format_number(payoff[1])})."
            )

    print(
        "\nMain conclusion:"
    )

    print(
        "High output is the dominant strategy for both firms. "
        "Therefore, both firms choose high output, producing the Nash "
        "equilibrium payoff of (2, 2)."
    )

    print(
        "They would both earn more at low output, where the payoff is "
        "(3, 3), but neither firm can trust the other to maintain low "
        "output because each could individually earn 5 by increasing "
        "production."
    )


# ============================================================
# MAIN ANALYSIS
# ============================================================

def analyze_game(
    payoff_matrix: Dict[Outcome, Payoff],
    firm1_strategies: List[Strategy],
    firm2_strategies: List[Strategy],
) -> None:
    """
    Runs the complete analysis.
    """

    validate_payoff_matrix(
        payoff_matrix,
        firm1_strategies,
        firm2_strategies,
    )

    display_payoff_matrix(
        payoff_matrix,
        firm1_strategies,
        firm2_strategies,
    )

    explain_all_scenarios(
        payoff_matrix,
        firm1_strategies,
        firm2_strategies,
    )

    explain_best_responses(
        payoff_matrix,
        firm1_strategies,
        firm2_strategies,
    )

    dominant_firm1 = find_strictly_dominant_strategy_firm1(
        payoff_matrix,
        firm1_strategies,
        firm2_strategies,
    )

    dominant_firm2 = find_strictly_dominant_strategy_firm2(
        payoff_matrix,
        firm1_strategies,
        firm2_strategies,
    )

    equilibria = find_nash_equilibria(
        payoff_matrix,
        firm1_strategies,
        firm2_strategies,
    )

    joint_best_outcomes, highest_combined_payoff = (
        find_joint_profit_maximum(payoff_matrix)
    )

    explain_nash_equilibrium(
        payoff_matrix,
        equilibria,
        firm1_strategies,
        firm2_strategies,
    )

    explain_prisoners_dilemma(
        payoff_matrix,
        equilibria,
        joint_best_outcomes,
        highest_combined_payoff,
    )

    print_final_summary(
        payoff_matrix,
        dominant_firm1,
        dominant_firm2,
        equilibria,
    )


def main() -> None:
    analyze_game(
        PAYOFF_MATRIX,
        FIRM_1_STRATEGIES,
        FIRM_2_STRATEGIES,
    )


if __name__ == "__main__":
    main()
