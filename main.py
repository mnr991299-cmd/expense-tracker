# main.py

from expense_manager import add_expense, show_expenses, total_expenses, filter_by_category, filter_by_month

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Show All Expenses")
    print("3. Show Total Expenses")
    print("4. Filter by Category")
    print("5. Filter by Month")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Amount must be a number! Try again.")
            continue
        description = input("Enter description: ")
        add_expense(date, category, amount, description)

    elif choice == "2":
        sort_choice = input("Sort by (date/amount/none): ").lower()
        if sort_choice not in ["date", "amount"]:
            sort_choice = None
        show_expenses(sort_by=sort_choice)

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        cat = input("Enter category to filter: ")
        filtered = filter_by_category(cat)
        show_expenses(filtered=filtered)
        total_expenses(filtered=filtered)

    elif choice == "5":
        try:
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (1-12): "))
            filtered = filter_by_month(month, year)
            show_expenses(filtered=filtered)
            total_expenses(filtered=filtered)
        except ValueError:
            print("Invalid input! Enter numeric values for month and year.")

    elif choice == "6":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-6.")