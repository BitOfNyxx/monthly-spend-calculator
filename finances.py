from helpers import finance_user_prompt


def input_starting_balance() -> float:
    return finance_user_prompt("Please input your starting balance: ")


def input_monthly_income() -> float:
    return finance_user_prompt("Please input your monthly income post deductions: ")


def balance_post_income(starting_balance: float, monthly_income: float) -> float:
    return starting_balance + monthly_income


def apr_monthly_rate(apr_percent: float) -> float:
    return (apr_percent / 100) / 12


def add_interest_to_balance(balance: float, monthly_rate: float) -> float:
    # Balance in this regards refers to the balance of the debt/loan/credit card etc
    return balance * monthly_rate
