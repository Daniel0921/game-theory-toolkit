# Cournot Calculus Explained

This guide explains the mathematics behind the **Cournot Competition Analyzer** in a step-by-step manner. The goal is not simply to solve equations, but to understand **why** each mathematical step is necessary and what it means economically.

---

# 1. The Economic Problem

Imagine three companies that all produce the exact same product.

Each company must decide **how many units to produce**.

Unlike perfect competition, every firm's production decision affects the market price.

If everyone produces more:

```text
Total Supply Increases
        ↓
Market Price Falls
        ↓
Revenue Per Unit Falls
```

If everyone produces less:

```text
Total Supply Decreases
        ↓
Market Price Rises
        ↓
Revenue Per Unit Increases
```

Every firm therefore faces a tradeoff.

- Producing more increases sales.
- Producing more also lowers the market price.
- Producing less keeps prices high but reduces sales.

The objective is to find the quantity that **maximizes profit**, not necessarily the quantity that produces the most units.

---

# 2. Building the Profit Function

Everything begins with the market demand equation.

```text
P = 100 − Q
```

where

```text
Q = q1 + q2 + q3
```

Substituting total market output into the demand equation gives

```text
P = 100 − q1 − q2 − q3
```

This tells us that every additional unit produced by any firm lowers the market price.

---

## Revenue

Firm 1 sells `q1` units.

Revenue is simply

```text
Revenue = Price × Quantity
```

Therefore,

```text
Revenue = P × q1
```

---

## Costs

Suppose Firm 1 has a constant marginal cost of **$20 per unit**.

Its production cost is

```text
Cost = 20 × q1
```

---

## Profit

Profit is always

```text
Profit = Revenue − Cost
```

Substituting everything together gives

```text
π1 = Pq1 − 20q1
```

Replacing **P** with the demand equation gives

```text
π1 = (100 − q1 − q2 − q3)q1 − 20q1
```

Expanding the brackets:

```text
π1 = 80q1 − q1² − q1q2 − q1q3
```

---

## Economic Interpretation

Each term tells a story.

```text
80q1
```

The profit generated from selling additional units.

```text
−q1²
```

Firm 1 hurts itself by producing too much because increased output lowers the market price.

```text
−q1q2
```

Firm 2's production hurts Firm 1.

```text
−q1q3
```

Firm 3's production also hurts Firm 1.

The profit function therefore captures both **competition** and **market pricing**.

---

# 3. Why We Take the Derivative

Imagine hiking to the top of a mountain.

- If the trail slopes upward, keep walking.
- If it slopes downward, you've already passed the top.
- At the very top, the slope is perfectly flat.

The derivative measures that slope.

In economics, the "mountain" is the firm's profit curve.

The derivative tells us

> **If Firm 1 produces one more unit, how will its profit change?**

Taking the derivative gives

```text
∂π1/∂q1 = 80 − 2q1 − q2 − q3
```

Notice how every term changes.

```text
80q1      → 80

−q1²      → −2q1

−q1q2     → −q2

−q1q3     → −q3
```

While taking the derivative, Firms 2 and 3 are treated as fixed.

Only Firm 1 is making a decision.

---

# 4. Finding the Profit-Maximizing Output

Once we know the slope of the profit curve, we simply find where that slope equals zero.

```text
80 − 2q1 − q2 − q3 = 0
```

Why zero?

Because

```text
Positive slope
```

means

```text
Producing more increases profit.
```

while

```text
Negative slope
```

means

```text
Producing more decreases profit.
```

The maximum occurs exactly where the slope changes from positive to negative.

That is why economists solve

```text
Derivative = 0
```

---

# 5. Building the Reaction Function

Now solve the previous equation for Firm 1's output.

Start with

```text
80 − 2q1 − q2 − q3 = 0
```

Move the rival quantities.

```text
2q1 = 80 − q2 − q3
```

Divide both sides by two.

```text
q1 = (80 − q2 − q3)/2
```

This equation is Firm 1's **reaction function**.

It tells Firm 1 exactly how much it should produce after observing what its competitors produce.

Applying the exact same process to the other firms gives

```text
q2 = (80 − q1 − q3)/2

q3 = (80 − q1 − q2)/2
```

Each firm now has its own best-response equation.

---

# 6. Solving the Nash Equilibrium

Because every firm is identical, we assume

```text
q1 = q2 = q3 = q
```

Substitute this into Firm 1's reaction function.

```text
q = (80 − q − q)/2
```

Simplify.

```text
q = (80 − 2q)/2
```

Multiply both sides by two.

```text
2q = 80 − 2q
```

Move all the quantities to one side.

```text
4q = 80
```

Finally,

```text
q = 20
```

Therefore,

```text
q1 = 20

q2 = 20

q3 = 20
```

Now compute market output.

```text
Q = 20 + 20 + 20 = 60
```

Price becomes

```text
P = 100 − 60 = 40
```

Each firm's profit becomes

```text
Profit = (40 − 20) × 20

Profit = 400
```

---

## Economic Interpretation

Every firm produces exactly 20 units.

Nobody wants to produce more.

Nobody wants to produce less.

Each firm is already making its best possible decision given what the others are doing.

---

# 7. Why the Second Derivative Matters

Finding where the first derivative equals zero does **not** automatically guarantee maximum profit.

A point where the first derivative equals zero could be:

- a maximum,
- a minimum,
- or a flat turning point.

To determine **which one we have**, we take the derivative **one more time**.

Recall that the first derivative was

```text
∂π1/∂q1 = 80 − 2q1 − q2 − q3
```

Now differentiate this equation with respect to `q1`.

### Step 1

Take the derivative of each term individually.

```text
80        → 0
```

The derivative of a constant is always zero.

```text
−2q1      → −2
```

The derivative of `−2q1` is simply `−2`.

```text
−q2       → 0
```

Since Firm 2's output is treated as a constant while Firm 1 changes its own production, its derivative is zero.

```text
−q3       → 0
```

Firm 3's output is also treated as a constant, so its derivative is zero as well.

### Step 2

Combine the results.

```text
∂²π1/∂q1² = 0 − 2 − 0 − 0
```

Simplify.

```text
∂²π1/∂q1² = −2
```

---

## What Does This Mean?

The second derivative tells us the **shape of the profit curve**.

Because

```text
−2 < 0
```

the profit curve bends downward.

```text
          Profit

             ▲
             │
         ● Maximum
        / \
       /   \
______/_____\________► Output
```

A downward-bending curve is called **concave**.

This means that as Firm 1 produces more output, the additional profit from producing one more unit gradually decreases until it eventually becomes negative.

Since the curve is concave, the point where the first derivative equals zero must be the **highest point on the curve**.

Therefore, the solution we found is a **maximum**, not a minimum.

---

### Economic Interpretation

The first derivative tells us **where the profit curve becomes flat**.

The second derivative tells us **whether that flat point is the top or the bottom of the curve**.

Because the second derivative equals **−2**, we know Firm 1's profit function is always concave. This confirms that the quantity calculated from the first-order condition is the **profit-maximizing output**.

---

# 8. Verifying the Equilibrium

Now plug the equilibrium quantities back into each firm's reaction function.

Firm 1

```text
q1 = (80 − 20 − 20)/2

q1 = 20
```

Firm 2

```text
q2 = (80 − 20 − 20)/2

q2 = 20
```

Firm 3

```text
q3 = (80 − 20 − 20)/2

q3 = 20
```

Every firm's chosen quantity equals its own best response.

That is exactly what defines a **Cournot-Nash Equilibrium**.

No single firm can increase profit by changing its output while every other firm keeps producing 20 units.

---

# 9. How the Python Script Does This Automatically

The analyzer performs exactly the same mathematics symbolically.

### Step 1

Construct the profit function.

```python
profit = (price - marginal_cost) * quantity - fixed_cost
```

### Step 2

Differentiate profit.

```python
first_derivative = sp.diff(profit, quantity)
```

### Step 3

Find the quantity where the derivative equals zero.

```python
reaction_function = sp.solve(
    sp.Eq(first_derivative, 0),
    quantity
)
```

### Step 4

Verify that the solution is actually a maximum.

```python
second_derivative = sp.diff(first_derivative, quantity)
```

### Step 5

Solve every firm's reaction function simultaneously.

The resulting solution is the **Cournot-Nash Equilibrium**.

The analyzer then

- computes profits,
- verifies best responses,
- performs deviation tests,
- compares monopoly and competitive outcomes,
- generates reaction-function graphs,
- exports a complete Markdown report.

---

# 10. Key Takeaways

The Cournot model teaches several important ideas.

✅ Firms compete by choosing **quantities**, not prices.

✅ Every firm's production affects the market price.

✅ Calculus identifies the quantity that maximizes profit.

✅ The first derivative finds the optimal quantity.

✅ The second derivative confirms it is a maximum.

✅ A reaction function describes a firm's best response.

✅ Solving every reaction function together produces the **Cournot-Nash Equilibrium**.

---

# Final Summary

The entire Cournot model can be summarized in one sentence:

> **Each firm chooses the production quantity that maximizes its own profit given what every other firm produces. When every firm is simultaneously choosing its best response, the market reaches a Cournot-Nash Equilibrium.**
