from bills import monthly_bills, remove_bills_from_balance
from debts import create_debt_list
from finances import (
    apr_monthly_rate,
    balance_post_income,
    input_monthly_income,
    input_starting_balance,
    interest_on_balance,
)


def main():
    print("Monthly Budget Calculator")

    starting_balance: float = input_starting_balance()
    print(f"Your starting balance: {starting_balance:.2f}")

    monthly_income: float = input_monthly_income()
    print(f"Your monthly income: {monthly_income:.2f}")

    new_balance: float = balance_post_income(starting_balance, monthly_income)
    print(f"Balance post income: {new_balance:.2f}")

    bills = monthly_bills()

    balance_after_bills = remove_bills_from_balance(new_balance, bills)
    print(f"Balance remaining after paying bills: {balance_after_bills:.2f}")

    debts = create_debt_list()

    if debts:
        print("Debt interest this month: ")
        for debt in debts:
            monthly_rate = apr_monthly_rate(debt.apr_percent)
            interest_accrued = interest_on_balance(debt.balance, monthly_rate)
            print(f"{debt.name} has accrued £{interest_accrued:.2f} this month")


if __name__ == "__main__":
    main()
