# save_a_buck_questions.py
from save_a_buck_user import User

class Questions(User):
    def __init__(self, firstname, lastname, email):
        super().__init__(firstname, lastname, email)
        # Financial Data
        self.yearly_salary = 0.0
        self.state_tax = 0.0
        self.federal_tax = 0.0
        self.contribution = 0.0
        
        # We use a dictionary to hold any number of expenses
        self.expenditures = {} 

    def ask_salary_questions(self):
        self.yearly_salary = float(input("What is your yearly salary? "))
        self.state_tax = float(input("What is your estimated state tax (%)? "))
        self.federal_tax = float(input("What is your estimated federal tax (%)? "))
        self.contribution = float(input("What percent do you contribute to retirement? "))

    def add_expenditures(self):
        """Allows user to add expenses until they type 'done'"""
        print("\n--- Enter your monthly expenditures ---")
        print("(Type 'done' when you are finished)")
        
        while True:
            item = input("Expense name (e.g., Rent, Car, Groceries): ").strip()
            if item.lower() == 'done':
                break
            
            try:
                amount = float(input(f"Monthly cost for {item}: "))
                # Add or update the item in our dictionary
                self.expenditures[item] = amount
            except ValueError:
                print("Please enter a valid number for the amount.")

    def show_spending_summary(self):
        """Prints out all recorded expenses and the total"""
        print(f"\n--- {self.firstname}'s Spending Summary ---")
        total = 0
        for item, amount in self.expenditures.items():
            print(f"- {item}: ${amount:,.2f}")
            total += amount
        print(f"Total Monthly Spending: ${total:,.2f}")

    