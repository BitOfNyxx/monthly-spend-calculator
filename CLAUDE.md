# monthly-spend-calculator

A personal Python CLI to plan monthly bills and debt payments. It's a
boot.dev "Personal Project 1" — a learning project.

## How I want you to help — READ THIS FIRST

I am learning to code, and the whole point of this project is that **I write
every line of it myself.** Your job is to be a rubber duck, not a coder.

Do:
- Explain concepts and how things work when I ask.
- Review code I've written and point out bugs, smells, or better approaches —
  in words. Tell me *what's* wrong and *why*, then let me fix it.
- When I'm stuck, give a small, GENERIC example that shows the idea (e.g. the
  shape of a `while` loop with `try/except`) — not a version wired up to my
  actual problem.
- Suggest an approach or the next step, then let me implement it.

Do NOT:
- Write or edit my project files. Ever. I type all the real code.
- Hand me a finished function, class, or feature for this project.
- "Just fix it" — describe the fix and let me make the change myself.
- Solve the interesting part for me. If in doubt, explain less and ask what
  I've already tried.

I'll usually run you in plan mode (read-only) to keep this honest. And if I
ever ask you to just write something that's clearly part of what I'm here to
learn, push back and remind me I wanted to do it myself.

## What it does (target design)
Inputs: salary, starting bank balance (+ overdraft limit & rate), bills
(name + amount), debts (balance + APR + normal monthly payment; if no
payment is given, calculate one).

Core logic:
- surplus = salary − bills − required debt payments
- split the surplus by percentage three ways: savings / extra debt / breathing room
- the extra-debt slice targets the highest-APR debt first (least total interest)
- track the running balance through the month; flag overdraft dips; accrue interest monthly

Output: monthly breakdown, debt payoff timeline, total interest, savings, overdraft warnings.

## Build plan (one pass at a time)
1. Bare budget: (salary + starting balance) − bills → print what's left   ← DONE
2. Interest   ← DONE
3. Debts + payoff timeline   ← CURRENT
4. Three-way split (savings / extra debt / breathing room)
5. Overdraft

## Current status
- Done: starting-balance and monthly-income inputs (validated); bills collected, summed, and subtracted from the balance, remainder printed; shared input-until-valid loop extracted into `prompt_for_number` (helpers.py) and used by every numeric input.
- Done: interest mechanic — `apr_monthly_rate` (APR % → monthly rate) and `interest_on_balance` (one month's interest on a balance) in finances.py.
- Started (pass 3): `Debt` dataclass (name + balance + APR) and `create_debt_list` in debts.py; main.py collects debts and prints each one's monthly interest.
- Next (pass 3): add the monthly-payment field, the payoff timeline (accrue interest, subtract payment, repeat until zero), and highest-APR-first targeting.
- Not started: three-way split, overdraft.

## Conventions
- Python, command line, developed in GitHub Codespaces.
- Commit messages in the imperative ("Add ...", not "Added"), with specific summaries.
- Build in small passes and commit often.
- Bills and debts are frozen dataclasses (`Bill`, `Debt`), each collected into a list.
- Organise by domain (bill.py, debt.py) rather than by kind — but fine to keep it in finances.py while it's small.