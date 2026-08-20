from helpers import prompt_for_number


def input_starting_balance() -> float:
    return prompt_for_number("Please input your starting balance: ")


def input_monthly_income() -> float:
    return prompt_for_number("Please input your monthly income post deductions: ")


def balance_post_income(starting_balance: float, monthly_income: float) -> float:
    return starting_balance + monthly_income


def apr_monthly_rate(apr_percent: float) -> float:
    return (apr_percent / 100) / 12


def interest_on_balance(balance: float, monthly_rate: float) -> float:
    # Balance in this regards refers to the balance of the debt/loan/credit card etc
    return balance * monthly_rate
