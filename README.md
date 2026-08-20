# monthly-spend-calculator

A small Python command-line tool to plan a month of bills and debt payments.
You enter your starting balance, monthly income, your bills, and your debts,
and it works out what's left and how much interest each debt accrues in a
month.

This is my **boot.dev "Personal Project 1"** — a learning project. The goal
isn't the tool; it's me getting better at writing Python.

## Status

Built in small passes, one at a time:

1. **Bare budget** — (income + starting balance) − bills → what's left ✅
2. **Interest** — APR → monthly rate, one month's interest on a balance ✅
3. **Debts + payoff timeline** — *in progress* (the `Debt` model and per-debt
   interest exist; monthly payments and the payoff timeline are next)
4. Three-way split (savings / extra debt / breathing room) — planned
5. Overdraft handling — planned

## Running it

```bash
python3 main.py
```

It'll prompt you for a starting balance, monthly income, each bill
(name + amount), and each debt (name + balance + APR), then print the
remaining balance and each debt's monthly interest.

## Layout

- `main.py` — the flow: collects input, prints the breakdown.
- `finances.py` — balances and the interest maths (`apr_monthly_rate`,
  `interest_on_balance`).
- `bills.py` — the `Bill` dataclass and bill collection.
- `debts.py` — the `Debt` dataclass and debt collection.
- `helpers.py` — `prompt_for_number`, the shared "keep asking until it's a
  valid number" input loop.

## How this was built — rubber-ducking, not vibe-coding

The whole point of this project is that **I write every line of the code
myself.** I used Claude (via Claude Code) strictly as a *rubber duck*, not as
a code generator. Concretely, that meant Claude was allowed to:

- explain concepts and how things work when I got stuck,
- review code I'd already written and point out bugs, smells, or better
  approaches **in words**,
- show me small, *generic* examples of a pattern (e.g. the shape of a
  `while` loop with `try/except`) — never a version wired up to my actual
  problem,
- suggest the next step and let me implement it.

And explicitly **not** to write, edit, or hand me finished functions,
classes, or features. When I once asked it to "just do it," it pushed back
and reminded me I wanted to write it myself. The full set of ground rules
lives in [`CLAUDE.md`](./CLAUDE.md).

### On AI-generated code

**No AI-generated application code is in this repository.** Every line of the
Python — every function, every fix, every refactor — was typed by me. Claude's
role was limited to explaining, reviewing, and suggesting in prose.

For full honesty: Claude did edit two **non-code** documentation files —
`CLAUDE.md` (project notes / status) and this `README.md` — and helped with a
one-off git history tidy-up. None of that is program logic. The code is mine.
