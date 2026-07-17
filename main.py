# Expense Tracker Application

expensesList = []  # list of all expenses in form dictionary
print("Welcome to the Expense Tracker Application!: Budget me kharch karo ")

while True:
    print("\n==== Menu ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please enter your choice (1-4): "))

    # ADD EXPENSE
    if choice == 1:
        date = input("Enter the date of expense (YYYY-MM-DD): ")
        category = input("Enter the category of expense (e.g., Food, Transport, Entertainment, EMI, Makeup): ")
        description = input("Enter the description of expense: ")
        amount = float(input("Enter the amount of expense: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expensesList.append(expense)
        print("\nExpense added successfully!")

    # VIEW ALL EXPENSES
    elif choice == 2:
        if len(expensesList) == 0:
            print("\nNo expenses recorded yet.")
        else:
            print("\n==== Your All Expenses ====")
            for count, expense in enumerate(expensesList, start=1):
                print(f"Expense Number {count} -> {expense['date']} , {expense['category']} , {expense['description']} , {expense['amount']}")

    # VIEW TOTAL EXPENSES
    elif choice == 3:
        total = sum(expense['amount'] for expense in expensesList)
        print("\nTotal Expenses:", total)

    # EXIT
    elif choice == 4:
        print("\nThank you for using the Expense Tracker Application. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")
