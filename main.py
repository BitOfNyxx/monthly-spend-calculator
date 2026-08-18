from finances import balance_post_income, input_monthly_income, input_starting_balance


def main():
    print("Monthly Budget Calculator")

    starting_balance: float = input_starting_balance()
    print(f"{starting_balance:.2f}")

    monthly_income: float = input_monthly_income()
    print(f"{monthly_income:.2f}")

    new_balance: float = balance_post_income(starting_balance, monthly_income)
    print(f"Balance post income: {new_balance:.2f}")


if __name__ == "__main__":
    main()


"""
Flow:

Inputs: Salary, Starting Balance, Bills
Output: Remaining Balance after bills are paid

Bill structure: (name, amount)
"""
