# 01 — Prisoner's Dilemma Analyzer

A Python-based educational tool that analyzes a two-firm prisoner's dilemma in an oligopoly market.

## Project Overview

This project evaluates how two competing firms make decisions between:

- Low output, which supports a higher market price
- High output, which increases market share but pushes the market price lower

The program explains every possible outcome, identifies each firm's best responses, detects dominant strategies, finds the pure-strategy Nash equilibrium, and compares individual incentives with the jointly beneficial outcome.

## Payoff Matrix

| Firm 1 / Firm 2 | Low Output | High Output |
|---|---:|---:|
| Low Output | (3, 3) | (0, 5) |
| High Output | (5, 0) | (2, 2) |

Each cell is written as:

```text
(Firm 1 payoff, Firm 2 payoff)
