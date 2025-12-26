# Expence Tracker Project

expenses = []  # List of expenses as dictionaries
print("Welcome to Expense Tracker")

while True:
    print("===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        date = input("Enter date: ")
        category = input("Enter category (food, travel, makeup, books): ")
        description = input("Enter details: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("\nExpense added successfully!")

    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses added.")
        else:
            print("=== Your Expenses ===")
            count = 1
            for eachExpense in expenses:
                print(f"Expense {count} -> {eachExpense['date']}, {eachExpense['category']}, {eachExpense['description']}, {eachExpense['amount']}")
                count += 1

    elif choice == 3:
        total = 0
        for eachExpense in expenses:
            total += eachExpense["amount"]
        print("\nTotal Expense =", total)

    elif choice == 4:
        print("Exiting Program")
        break

    else:
        print("Invalid Choice!")
