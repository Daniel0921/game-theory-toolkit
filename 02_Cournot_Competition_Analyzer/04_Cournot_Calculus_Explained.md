# Cournot Competition Calculus Explained

This document explains the calculus used in the Cournot Competition Analyzer in clear, step-by-step terms.

The calculus is doing one basic job:

> **Find the production quantity where each firm's profit stops increasing and begins decreasing.**

The example below uses three identical firms.

---

## 1. Start with Market Demand

We assumed:

\[
P = 100 - Q
\]

Total output is the combined production of all three firms:

\[
Q = q_1 + q_2 + q_3
\]

Therefore:

\[
P = 100 - q_1 - q_2 - q_3
\]

This means that as the firms collectively produce more, the market price falls.

For example:

- If total output is 40, price is 60.
- If total output is 60, price is 40.
- If total output is 80, price is 20.

---

## 2. Build Firm 1's Profit Equation

Firm 1's profit is:

\[
\text{Profit} = \text{Revenue} - \text{Cost}
\]

Firm 1 produces \(q_1\) units. Its revenue is:

\[
Pq_1
\]

Its marginal cost is 20 per unit, so its production cost is:

\[
20q_1
\]

Therefore:

\[
\pi_1 = Pq_1 - 20q_1
\]

Substitute the market-price equation:

\[
\pi_1 = (100 - q_1 - q_2 - q_3)q_1 - 20q_1
\]

This is Firm 1's profit function.

---

## 3. Simplify the Profit Function

Distribute \(q_1\):

\[
\pi_1
=
100q_1 - q_1^2 - q_1q_2 - q_1q_3 - 20q_1
\]

Combine \(100q_1 - 20q_1\):

\[
\pi_1
=
80q_1 - q_1^2 - q_1q_2 - q_1q_3
\]

In ordinary language:

- \(80q_1\) represents the basic gain from selling more units above marginal cost.
- \(-q_1^2\) captures the price reduction caused by Firm 1's own production.
- \(-q_1q_2\) and \(-q_1q_3\) capture how rival production lowers the price Firm 1 receives.

Firm 1 wants to produce more, but not endlessly. Additional production increases sales while also pushing the market price down.

---

## 4. Take the First Derivative

Differentiate Firm 1's profit with respect to \(q_1\):

\[
\frac{\partial \pi_1}{\partial q_1}
=
80 - 2q_1 - q_2 - q_3
\]

The derivative tells us:

> **How much Firm 1's profit changes when Firm 1 produces one additional small unit, assuming Firms 2 and 3 do not change their quantities.**

The partial-derivative symbol \(\partial\) is used because the profit equation contains several variables, but we are changing only \(q_1\).

Each term changes as follows:

\[
80q_1 \rightarrow 80
\]

\[
-q_1^2 \rightarrow -2q_1
\]

\[
-q_1q_2 \rightarrow -q_2
\]

\[
-q_1q_3 \rightarrow -q_3
\]

Firm 2's and Firm 3's quantities are treated as fixed numbers while Firm 1 makes its decision.

---

## 5. Set the Derivative Equal to Zero

We use:

\[
80 - 2q_1 - q_2 - q_3 = 0
\]

Why set it equal to zero?

Imagine Firm 1's profit as a hill:

- Before the top, producing slightly more increases profit.
- At the top, producing slightly more has no immediate benefit.
- After the top, producing more reduces profit.

The derivative measures the slope of that hill. At the highest point, the slope equals zero.

A positive derivative means:

> Firm 1 should produce more.

A negative derivative means:

> Firm 1 is producing too much and should produce less.

A derivative of zero means:

> Firm 1 is at its profit-maximizing quantity, given its rivals' output.

---

## 6. Solve for Firm 1's Best Response

Start with:

\[
80 - 2q_1 - q_2 - q_3 = 0
\]

Move the rival quantities to the other side:

\[
2q_1 = 80 - q_2 - q_3
\]

Divide by 2:

\[
q_1 = \frac{80 - q_2 - q_3}{2}
\]

This is Firm 1's **reaction function**, also called its **best-response function**.

It tells Firm 1 how much to produce for every possible combination of rival output.

Suppose Firms 2 and 3 each produce 20:

\[
q_1 = \frac{80 - 20 - 20}{2}
\]

\[
q_1 = \frac{40}{2} = 20
\]

When the other firms each produce 20 units, Firm 1's best response is also 20 units.

---

## 7. Repeat the Process for the Other Firms

Because all three firms have the same cost structure, their equations have the same form:

\[
q_1 = \frac{80 - q_2 - q_3}{2}
\]

\[
q_2 = \frac{80 - q_1 - q_3}{2}
\]

\[
q_3 = \frac{80 - q_1 - q_2}{2}
\]

Each firm's best quantity depends on what the other two firms produce.

This creates strategic interdependence:

- If rivals produce more, a firm's best response is to produce less.
- If rivals produce less, a firm's best response is to produce more.

---

## 8. Solve All Three Equations Together

Because the firms are identical, we look for a symmetric equilibrium:

\[
q_1 = q_2 = q_3 = q
\]

Substitute \(q\) for all three firms in one reaction function:

\[
q = \frac{80 - q - q}{2}
\]

Combine the two rival quantities:

\[
q = \frac{80 - 2q}{2}
\]

Multiply both sides by 2:

\[
2q = 80 - 2q
\]

Add \(2q\) to both sides:

\[
4q = 80
\]

Divide by 4:

\[
q = 20
\]

Therefore:

\[
q_1 = q_2 = q_3 = 20
\]

---

## 9. Calculate Total Output and Price

Total output is:

\[
Q = 20 + 20 + 20 = 60
\]

Market price is:

\[
P = 100 - 60 = 40
\]

Each firm sells 20 units at a price of 40 and has a marginal cost of 20.

Profit per firm is:

\[
\pi_i = (40 - 20)(20)
\]

\[
\pi_i = 400
\]

| Measure | Result |
|---|---:|
| Firm 1 output | 20 |
| Firm 2 output | 20 |
| Firm 3 output | 20 |
| Total output | 60 |
| Market price | 40 |
| Profit per firm | 400 |

---

## 10. Check the Second Derivative

The first derivative identifies a point where the slope equals zero. However, that point could theoretically be a maximum or a minimum.

Differentiate the first derivative again:

\[
\frac{\partial^2\pi_1}{\partial q_1^2} = -2
\]

The second derivative is negative.

That means Firm 1's profit curve bends downward, like an upside-down bowl. Therefore, the stationary point is the top of the curve—a profit maximum.

A useful rule is:

- Positive second derivative: the curve bends upward and the point is likely a minimum.
- Negative second derivative: the curve bends downward and the point is likely a maximum.

The value \(-2\) confirms that the quantity of 20 maximizes profit.

---

## 11. Verify the Nash Equilibrium

At the proposed equilibrium:

\[
q_1 = q_2 = q_3 = 20
\]

Check Firm 1:

\[
q_1 = \frac{80 - 20 - 20}{2} = 20
\]

Check Firm 2:

\[
q_2 = \frac{80 - 20 - 20}{2} = 20
\]

Check Firm 3:

\[
q_3 = \frac{80 - 20 - 20}{2} = 20
\]

Every firm is choosing its best response to the other firms.

That is why this is a **Cournot-Nash equilibrium**:

> No firm can increase its profit by changing its own output alone while the other two firms continue producing 20 units.

---

## 12. Test a Small Deviation

Firm 1 earns 400 at 20 units.

Suppose Firm 1 increases production to 21 while Firms 2 and 3 remain at 20.

Total output becomes:

\[
Q = 21 + 20 + 20 = 61
\]

Price becomes:

\[
P = 100 - 61 = 39
\]

Firm 1's profit becomes:

\[
\pi_1 = (39 - 20)(21) = 399
\]

Its profit falls from 400 to 399.

Now suppose Firm 1 decreases output to 19:

\[
Q = 19 + 20 + 20 = 59
\]

\[
P = 100 - 59 = 41
\]

\[
\pi_1 = (41 - 20)(19) = 399
\]

Again, profit falls to 399.

| Firm 1 quantity | Profit |
|---:|---:|
| 19 | 399 |
| **20** | **400** |
| 21 | 399 |

This gives a concrete interpretation of the calculus. The derivative found the exact center of the profit peak.

---

## What the Python Script Is Doing

SymPy performs these steps automatically for every firm.

First, the script constructs the profit equation:

```python
profit = (price - marginal_cost) * quantity - fixed_cost
```

Then it calculates the first derivative:

```python
first_derivative = sp.diff(profit, quantity)
```

This asks:

> How does profit change when this firm changes its own output?

Next, it solves the first-order condition:

```python
reaction_function = sp.solve(
    sp.Eq(first_derivative, 0),
    quantity
)
```

This asks:

> What quantity makes the change in profit equal to zero?

Finally, it calculates the second derivative:

```python
second_derivative = sp.diff(first_derivative, quantity)
```

This checks:

> Is the calculated point the top of the profit curve?

---

## Overall Summary

The script:

1. Creates each firm's profit equation.
2. Differentiates profit to measure the benefit of producing slightly more.
3. Finds where that benefit reaches zero.
4. Confirms that the result is a profit maximum.
5. Solves all firms' reaction functions together.
6. Verifies that every firm is choosing a best response.
7. Confirms that no firm benefits from changing output alone.

In one sentence:

> The calculus finds each firm's profit-maximizing output, and solving those decisions together produces the Cournot-Nash equilibrium.
