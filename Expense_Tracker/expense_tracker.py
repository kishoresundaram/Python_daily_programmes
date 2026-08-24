print("******** EXPENSE TRACKER ********")

expenses = []

menu = 0

while menu != 5:

    print("\n1 → Add Expense")
    print("2 → Display Expenses")
    print("3 → Show Total Expense")
    print("4 → Show Categories")
    print("5 → Exit")

    menu = int(input("Enter your option: "))

    if menu == 1:

        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "item": item,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        print("Expense added successfully!")

    elif menu == 2:

        if len(expenses) == 0:
            print("\nNo expenses available.")

        else:
            print("\n******** EXPENSES ********")

            for expense in expenses:
                print("Item     :", expense["item"])
                print("Amount   :", expense["amount"])
                print("Category :", expense["category"])
                print("-------------------------")

    elif menu == 3:

        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total Expense:", total)

    elif menu == 4:

        categories = set()

        for expense in expenses:
            categories.add(expense["category"])

        print("\n******** CATEGORIES ********")

        for category in categories:
            print(category)

    elif menu == 5:

        print("\nThank you for using Expense Tracker!")

    else:

        print("\nPlease enter a correct option.")