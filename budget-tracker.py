budget = 0
recent_expenses_length = 5
recent_expenses = []

def add_expense(amount):
    global budget
    if amount > budget:
        print("Insufficient budget to add this expense.")
        return False
    budget -= amount
    return True

def add_income(amount):
    global budget
    budget += amount

def get_recent_expenses():
    return recent_expenses[-recent_expenses_length:]

def display_menu():
    print("==== Budget Tracker ====")
    print("Current Budget: $", budget)
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Expenses")
    print("4. Exit")

    return input("Choice: ")

def track_expense():
    print("Enter the category of the expense (e.g., Food, Transport, Entertainment): ")
    category = input("Category: ")
    print("Enter the amount of the expense: ")
    amount = input("Amount: $")
    if not amount.isdigit():
        print("Invalid input. Please enter a numeric value.")
        return
    print(f"Expense of ${amount} added to category: {category}")
    add_expense(int(amount))
    recent_expenses.append({category: int(amount)})

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            track_expense()
        elif choice == '2':
            amount = input("Enter income amount: $")
            if not amount.isdigit():
                print("Invalid input. Please enter a numeric value.")
                continue
            add_income(int(amount))
            print("Income added. New budget: $", budget)
        elif choice == '3':
            expenses = get_recent_expenses()
            print("Recent Expenses: ", expenses)
        elif choice == '4':
            print("Exiting Budget Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()