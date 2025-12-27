# save_a_buck_calculations.py
from save_a_buck_questions import Questions

class Calculations(Questions):
    def __init__(self, firstname, lastname, email):
        super().__init__(firstname, lastname, email)

    def calculate_take_home_pay(self):
        
        # 1. Calculate total tax and retirement percentage
        total_deductions_percent = (self.state_tax + self.federal_tax + self.contribution) / 100
        
        # 2. Calculate annual and then monthly take-home
        annual_deduction = self.yearly_salary * total_deductions_percent
        annual_take_home = self.yearly_salary - annual_deduction
        monthly_take_home = annual_take_home / 12
        
        return monthly_take_home

    def calculate_remaining_budget(self):
        # 3. Subtracts expenditures from the take-home pay.
        monthly_income = self.calculate_take_home_pay()
        total_expenses = sum(self.expenditures.values())
        remaining = monthly_income - total_expenses
        
        print(f"\n--- Financial Analysis for {self.firstname} ---")
        print(f"Monthly Take-Home: ${monthly_income:,.2f}")
        print(f"Total Expenses:    ${total_expenses:,.2f}")
        print(f"Remaining Budget:  ${remaining:,.2f}")
        
        if remaining < 0:
            print("Warning: Your expenses exceed your take-home pay!")

    



