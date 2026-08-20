from dataclasses import dataclass

from helpers import prompt_for_number


@dataclass(frozen=True)
class Bill:
    name: str
    bill_amount: float


def monthly_bills() -> list[Bill]:
    bill_list = []
    while True:
        bill_name = input("Please input the name of the bill (leave blank to finish): ")

        if not bill_name:
            break

        bill_amount = prompt_for_number("Please input the bill amount: ")

        bill_list.append(Bill(name=bill_name, bill_amount=bill_amount))

    return bill_list


def remove_bills_from_balance(current_balance: float, bills: list[Bill]) -> float:
    for bill in bills:
        current_balance -= bill.bill_amount
    return current_balance
