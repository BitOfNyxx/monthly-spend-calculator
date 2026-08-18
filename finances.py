from helpers import finance_user_prompt


def input_starting_balance() -> float:
    return finance_user_prompt("Please input your starting balance: ")


def input_monthly_income() -> float:
    return finance_user_prompt("Please input your monthly income post deductions: ")


def balance_post_income(starting_balance: float, monthly_income: float) -> float:
    return starting_balance + monthly_income
