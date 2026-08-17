def input_starting_balance() -> float:
    while True:
        try:
            return round(float(input("Please input your starting balance: ")))
        except ValueError:
             print("Value entered is not a valid number, please try again.")

def input_monthly_income() -> float:
        try:
            return float(input("Please input your monthly income post deductions: "))
        except ValueError:
            print("Value entered is not a valid number, please try again.")
            
def balance_post_income(starting_balance: float, monthly_income: float) -> float:
    return starting_balance + monthly_income