# 02 — Cournot Competition Analyzer

A dynamic Python project that models quantity competition among two or three firms.

## Project Overview

In a Cournot market, firms choose production quantities independently and simultaneously. Total industry output determines the market price, so each firm's decision affects both its own sales and the profitability of every rival.

This analyzer uses symbolic calculus and numerical equilibrium solving to show how firms derive best responses and arrive at a Cournot-Nash equilibrium.

## Main Features

- Supports **two or three firms**
- Uses linear inverse demand: `P(Q) = a - bQ`
- Allows different marginal and fixed costs for each firm
- Builds symbolic profit functions with SymPy
- Calculates first and second derivatives
- Derives reaction functions
- Solves simultaneous first-order conditions
- Enforces nonnegative quantities
- Detects zero-output corner solutions
- Verifies every firm's best response
- Tests unilateral output deviations
- Compares Cournot with monopoly and perfect competition
- Generates reaction-function charts
- Exports a detailed Markdown analysis automatically

## Default Example

```text
P(Q) = 100 - Q
MC1 = MC2 = MC3 = 20
Fixed costs = 0
```

| Result | Value |
|---|---:|
| Firm 1 output | 20.00 |
| Firm 2 output | 20.00 |
| Firm 3 output | 20.00 |
| Total output | 60.00 |
| Market price | 40.00 |
| Profit per firm | 400.00 |

## Economic Model

```text
Q = q1 + q2 + ... + qn
P(Q) = a - bQ
Ci(qi) = ci × qi + Fi
πi = [P(Q) - ci] × qi - Fi
```

The analyzer differentiates profit with respect to each firm's own quantity:

```text
∂πi/∂qi = a - ci - 2bqi - bΣqj
```

The reaction function is:

```text
qi = [a - ci - bΣqj] / 2b
```

The second derivative is:

```text
∂²πi/∂qi² = -2b
```

Because `b > 0`, the second derivative is negative and the first-order condition identifies a maximum.

## Nash Equilibrium

The Cournot-Nash equilibrium is the simultaneous intersection of all firms' reaction functions. At that point:

- Every firm is selecting its best response
- Rival quantities are treated as fixed
- No firm can increase profit by changing output alone
- All first-order conditions hold simultaneously

## Installation

```bash
pip install -r requirements.txt
```

## Run the Default Example

```bash
python cournot_competition_analyzer.py
```

## Run a Custom Market

```bash
python cournot_competition_analyzer.py --interactive
```

You can enter the number of firms, demand parameters, marginal costs, fixed costs, and the deviation-test size.

## Concepts Demonstrated

- Cournot competition
- Oligopoly
- Quantity competition
- Profit maximization
- Partial derivatives
- First- and second-order conditions
- Reaction functions
- Simultaneous equations
- Nash equilibrium
- Corner solutions
- Comparative market structures

## Author

Daniel Pineau
