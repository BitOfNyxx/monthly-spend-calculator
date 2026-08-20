from dataclasses import dataclass

from helpers import prompt_for_number


@dataclass(frozen=True)
class Debt:
    name: str
    balance: float
    apr_percent: float


def create_debt_list() -> list[Debt]:
    debt_list = []
    while True:
        debt_name = input("Please input the name of the debt (leave blank to finish): ")

        if not debt_name:
            break

        debt_balance = prompt_for_number("Please input the debt balance: ")
        debt_apr_percent = prompt_for_number(
            "Please input APR of the debt as a percentage: "
        )
        debt_list.append(
            Debt(name=debt_name, balance=debt_balance, apr_percent=debt_apr_percent)
        )

    return debt_list
