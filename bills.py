from dataclasses import dataclass


@dataclass(frozen=True)
class Bill:
    name: str
    bill_amount: float


def monthly_bills() -> list[Bill]:
    bill_list = []
    while True:
        bill_name = str(
            input("Please input the name of the bill (leave blank to finish): ")
        )
        if not bill_name:
            break
        while True:
            try:
                bill_amount = float(input("Please input the bill amount: "))
                break
            except ValueError:
                print("Value entered is not a valid number, please try again.")
                continue
        bill_list.append(Bill(name=bill_name, bill_amount=bill_amount))

    return bill_list


def remove_bills_from_balance(current_balance: float, bills: list[Bill]) -> float:
    for bill in bills:
        current_balance -= bill.bill_amount
    return current_balance
