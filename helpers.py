def finance_user_prompt(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("This value is not valid. Please try again.")
