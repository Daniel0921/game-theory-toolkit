# Cournot Competition Analyzer — Example Output

This report was generated automatically by `cournot_competition_analyzer.py`.

## 1. Market Configuration

- Firms: **3**
- Inverse demand: **P(Q) = 100.00 - 1.00Q**
- Marginal costs: **20.00, 20.00, 20.00**
- Fixed costs: **0.00, 0.00, 0.00**

Total output is the sum of all firms' quantities:

$$
Q = q_1 + q_2 + q_3
$$

## 2. Profit Functions

### Firm 1

$$
\pi_1 = - q_{1}^{2} - q_{1} q_{2} - q_{1} q_{3} + 80 q_{1}
$$

Firm 1 earns revenue from its own quantity, but every firm's output lowers the common market price. Fixed cost affects accounting profit but does not alter the reaction function.

### Firm 2

$$
\pi_2 = - q_{1} q_{2} - q_{2}^{2} - q_{2} q_{3} + 80 q_{2}
$$

Firm 2 earns revenue from its own quantity, but every firm's output lowers the common market price. Fixed cost affects accounting profit but does not alter the reaction function.

### Firm 3

$$
\pi_3 = - q_{1} q_{3} - q_{2} q_{3} - q_{3}^{2} + 80 q_{3}
$$

Firm 3 earns revenue from its own quantity, but every firm's output lowers the common market price. Fixed cost affects accounting profit but does not alter the reaction function.

## 3. Calculus and Reaction Functions

Each firm treats rival quantities as fixed, differentiates its profit with respect to its own quantity, and sets the derivative equal to zero.

### Firm 1

First derivative:

$$
\frac{\partial \pi_1}{\partial q_1} = - 2 q_{1} - q_{2} - q_{3} + 80
$$

Reaction function:

$$
q_1 = - \frac{q_{2}}{2} - \frac{q_{3}}{2} + 40
$$

Second derivative:

$$
\frac{\partial^2 \pi_1}{\partial q_1^2} = -2
$$

The second derivative is negative because the demand slope is positive. Therefore, the first-order condition identifies a profit maximum.

### Firm 2

First derivative:

$$
\frac{\partial \pi_2}{\partial q_2} = - q_{1} - 2 q_{2} - q_{3} + 80
$$

Reaction function:

$$
q_2 = - \frac{q_{1}}{2} - \frac{q_{3}}{2} + 40
$$

Second derivative:

$$
\frac{\partial^2 \pi_2}{\partial q_2^2} = -2
$$

The second derivative is negative because the demand slope is positive. Therefore, the first-order condition identifies a profit maximum.

### Firm 3

First derivative:

$$
\frac{\partial \pi_3}{\partial q_3} = - q_{1} - q_{2} - 2 q_{3} + 80
$$

Reaction function:

$$
q_3 = - \frac{q_{1}}{2} - \frac{q_{2}}{2} + 40
$$

Second derivative:

$$
\frac{\partial^2 \pi_3}{\partial q_3^2} = -2
$$

The second derivative is negative because the demand slope is positive. Therefore, the first-order condition identifies a profit maximum.

## 4. Cournot-Nash Equilibrium

| Firm | Quantity | Marginal cost | Fixed cost | Variable profit | Accounting profit |
|---:|---:|---:|---:|---:|---:|
| Firm 1 | 20.00 | 20.00 | 0.00 | 400.00 | 400.00 |
| Firm 2 | 20.00 | 20.00 | 0.00 | 400.00 | 400.00 |
| Firm 3 | 20.00 | 20.00 | 0.00 | 400.00 | 400.00 |

- Total market output: **60.00**
- Market price: **40.00**
- Total accounting profit: **1,200.00**

## 5. Best-Response Verification

| Firm | Equilibrium quantity | Calculated best response | Verified? |
|---:|---:|---:|:---:|
| Firm 1 | 20.00 | 20.00 | Yes |
| Firm 2 | 20.00 | 20.00 | Yes |
| Firm 3 | 20.00 | 20.00 | Yes |

Every firm is choosing its profit-maximizing quantity given its rivals' quantities. No firm can improve by changing output alone, so the solution is a Cournot-Nash equilibrium.

## 6. Unilateral Deviation Tests

Each firm is tested at **±1.00 unit(s)** from equilibrium.

| Firm | Equilibrium q | Equilibrium profit | Lower q | Lower-q profit | Higher q | Higher-q profit |
|---:|---:|---:|---:|---:|---:|---:|
| Firm 1 | 20.00 | 400.00 | 19.00 | 399.00 | 21.00 | 399.00 |
| Firm 2 | 20.00 | 400.00 | 19.00 | 399.00 | 21.00 | 399.00 |
| Firm 3 | 20.00 | 400.00 | 19.00 | 399.00 | 21.00 | 399.00 |

## 7. Market-Structure Comparison

| Structure | Total output | Price | Meaning |
|---|---:|---:|---|
| Joint-profit/monopoly benchmark | 40.00 | 60.00 | Output chosen to maximize joint variable profit using the lowest-cost technology. |
| Cournot competition | 60.00 | 40.00 | Firms choose output strategically and independently. |
| Perfect-competition benchmark | 80.00 | 20.00 | Price is pushed to the lowest constant marginal cost in this simplified benchmark. |

## 8. Economic Interpretation

A Cournot firm faces a tradeoff. Producing more creates additional sales, but it also increases total market output and lowers the market price on every unit the firm sells. The reaction function gives the quantity that best balances those effects for each possible level of rival output.

At equilibrium, all reaction functions are satisfied simultaneously. The outcome is stable against unilateral deviations even though a coordinated industry might prefer the lower-output monopoly benchmark.

## 9. Visualizations

With three firms, the reaction functions occupy three-dimensional strategy space. These charts show pairwise conditional reaction functions while holding the third firm at its equilibrium quantity.

![Firms 1 and 2](./reaction_functions_firms_1_2_holding_firm_3_fixed.png)

![Firms 1 and 3](./reaction_functions_firms_1_3_holding_firm_2_fixed.png)

![Firms 2 and 3](./reaction_functions_firms_2_3_holding_firm_1_fixed.png)
