import datetime

class ExpenseTracker:
    def __init__(self):
        self.transactions = []  

    def add_income(self, amount, source):
        self.transactions.append({
            "type": "Income",
            "amount": amount,
            "category": source,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Income of ₹{amount} from '{source}' added successfully!")

    def add_expense(self, amount, category, description):
        self.transactions.append({
            "type": "Expense",
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Expense of ₹{amount} for '{category}' added successfully!")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions to display!")
            return

        print("\nAll Transactions:")
        print("{:<10} {:<10} {:<15} {:<30} {:<20}".format(
            "Type", "Amount", "Category", "Description", "Date"))
        print("-" * 85)
        for transaction in self.transactions:
            print("{:<10} {:<10} {:<15} {:<30} {:<20}".format(
                transaction["type"],
                f"₹{transaction['amount']}",
                transaction["category"],
                transaction.get("description", "-"),
                transaction["date"]
            ))

    def view_balance(self):
        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "Income")
        total_expense = sum(t["amount"] for t in self.transactions if t["type"] == "Expense")
        balance = total_income - total_expense
        print(f"\nTotal Income: ₹{total_income}")
        print(f"Total Expense: ₹{total_expense}")
        print(f"Current Balance: ₹{balance}")

    def generate_report(self):
        if not self.transactions:
            print("No data available to generate a report!")
            return

        expenses_by_category = {}
        for t in self.transactions:
            if t["type"] == "Expense":
                category = t["category"]
                expenses_by_category[category] = expenses_by_category.get(category, 0) + t["amount"]

        print("\nExpense Report by Category:")
        for category, total in expenses_by_category.items():
            print(f"{category}: ₹{total}")

        self.view_balance()

    def delete_transaction(self):
        if not self.transactions:
            print("No transactions to delete!")
            return

        self.view_transactions()
        try:
            index = int(input("\nEnter the transaction number to delete (1-based index): ")) - 1
            if 0 <= index < len(self.transactions):
                removed = self.transactions.pop(index)
                print(f"Transaction '{removed['type']} of ₹{removed['amount']}' deleted successfully!")
            else:
                print("Invalid transaction number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Generate Report")
        print("6. Delete Transaction")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            amount = float(input("Enter income amount: ₹"))
            source = input("Enter source of income: ")
            tracker.add_income(amount, source)
        elif choice == "2":
            amount = float(input("Enter expense amount: ₹"))
            category = input("Enter category (e.g., Food, Transport): ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == "3":
            tracker.view_transactions()
        elif choice == "4":
            tracker.view_balance()
        elif choice == "5":
            tracker.generate_report()
        elif choice == "6":
            tracker.delete_transaction()
        elif choice == "7":
            print("Thank you for using the Personal Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
