# Prisoner's Dilemma Analysis Report

## Payoff Matrix

| Firm 1 \ Firm 2 | Low Output | High Output |
|-----------------|-----------:|------------:|
| **Low Output**  | (3, 3) | (0, 5) |
| **High Output** | (5, 0) | (2, 2) |

---

## Scenario 1 — Both Firms Choose Low Output

### Decisions

- Firm 1 chooses **Low Output**.
- Firm 2 chooses **Low Output**.

### Payoffs

| Firm | Payoff |
|------|-------:|
| Firm 1 | **3** |
| Firm 2 | **3** |
| Combined | **6** |

### Economic Interpretation

Both firms voluntarily restrict production. Because total market output remains relatively low, the market price stays high, allowing both firms to earn healthy profits.

This outcome maximizes the firms' combined profit and represents the cooperative (joint-profit-maximizing) outcome.

### Incentive to Deviate

Although this outcome benefits both firms, it is unstable.

- Firm 1 could increase its payoff from **3 → 5** by increasing output while Firm 2 continues restricting production.
- Firm 2 faces exactly the same temptation.

Because both firms have an incentive to deviate, this outcome is difficult to sustain.

---

## Scenario 2 — Firm 1 Chooses Low Output, Firm 2 Chooses High Output

### Decisions

- Firm 1 chooses **Low Output**.
- Firm 2 chooses **High Output**.

### Payoffs

| Firm | Payoff |
|------|-------:|
| Firm 1 | **0** |
| Firm 2 | **5** |
| Combined | **5** |

### Economic Interpretation

Firm 1 limits production while Firm 2 expands production.

Firm 2 benefits from capturing additional market share while still enjoying the relatively high market price created by Firm 1's restraint.

Firm 1 bears the cost of cooperating while Firm 2 benefits from defecting.

### Incentive to Deviate

- Firm 1 would increase its payoff from **0 → 2** by switching to High Output.
- Firm 2 would decrease its payoff from **5 → 3** by switching to Low Output.

---

## Scenario 3 — Firm 1 Chooses High Output, Firm 2 Chooses Low Output

*(Mirror image of Scenario 2.)*

...

---

## Scenario 4 — Both Firms Choose High Output

### Decisions

- Firm 1 chooses **High Output**.
- Firm 2 chooses **High Output**.

### Payoffs

| Firm | Payoff |
|------|-------:|
| Firm 1 | **2** |
| Firm 2 | **2** |
| Combined | **4** |

### Economic Interpretation

Both firms aggressively increase production.

Because total market output rises, market prices fall.

Neither firm allows the other to gain a competitive advantage, but both earn less profit than they would have earned under mutual cooperation.

### Incentive to Deviate

Neither firm benefits from reducing output alone.

Doing so would reduce its payoff from **2 → 0**.

Therefore, this outcome is strategically stable.

---

# Best-Response Analysis

## Firm 1

| Firm 2 Chooses | Low Output | High Output | Best Response |
|----------------|-----------:|------------:|---------------|
| Low Output | 3 | **5** | **High Output** |
| High Output | 0 | **2** | **High Output** |

Firm 1's best response is **High Output**, regardless of what Firm 2 does.

---

## Firm 2

| Firm 1 Chooses | Low Output | High Output | Best Response |
|----------------|-----------:|------------:|---------------|
| Low Output | 3 | **5** | **High Output** |
| High Output | 0 | **2** | **High Output** |

Firm 2's best response is also **High Output**, regardless of what Firm 1 does.

---

# Nash Equilibrium

## Equilibrium Outcome

| Firm | Strategy |
|------|----------|
| Firm 1 | **High Output** |
| Firm 2 | **High Output** |

### Payoffs

```text
(2, 2)
