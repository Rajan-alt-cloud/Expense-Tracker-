# Expense Tracker Application

expensesList = []  # list of all expenses in form dictionary
print("Welcome to the Expense Tracker Application!: Budget me kharch karo ")

while True:
    print("\n==== Menu ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = int(input("Please enter your choice (1-5): "))

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

    # DELETE EXPENSE
    elif choice == 4:
        if len(expensesList) == 0:
            print("\nNo expenses available to delete.")
        else:
            print("\n==== Your All Expenses ====")
            for count, expense in enumerate(expensesList, start=1):
                print(f"{count}. {expense['date']} | {expense['category']} | {expense['description']} | ₹{expense['amount']}")

            expenseNumber = int(input("\nEnter the expense number to delete: "))

            if 1 <= expenseNumber <= len(expensesList):
                deletedExpense = expensesList.pop(expenseNumber - 1)
                print(f"\nExpense '{deletedExpense['description']}' deleted successfully!")
            else:
                print("\nInvalid expense number.")

    # EXIT
    elif choice == 5:
        print("\nThank you for using the Expense Tracker Application. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")
