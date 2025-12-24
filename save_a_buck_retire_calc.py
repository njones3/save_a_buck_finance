class Save_a_buck:
    
    class User:
        def __init__(self, firstname, lastname, email):
            self.firstname = firstname
            self.lastname = lastname
            self.email = email
            # Financial Data
            self.age = 0
            self.salary = 0.0
            self.retirement_age = 0
            self.annual_raise = 0.0
            self.contribution = 0.0
            self.match = 0.0
            self.personal_contribution = 0.0
            self.rate_return = 0.0
            self.state = 0.0
            self.federal = 0.0
            self.savings = 0.0

    class Questions:
        @classmethod
        def create_new_user(cls):
            print("---- STEP 1: Create Account ----")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            return Save_a_buck.User(fname, lname, email)

        @classmethod
        def complete_profile(cls, user_obj):
            print(f"\n---- STEP 2: Financial information for {user_obj.firstname} ----")
            try:
                user_obj.age = int(input("What is your age? "))
                user_obj.salary = float(input("Current yearly salary: "))
                user_obj.retirement_age = int(input("Desired retirement age? "))
                
                print("\nNote: Enter percentages as decimals (e.g., 0.03 for 3%)")
                user_obj.annual_raise = float(input("Expected annual pay raise %: "))
                user_obj.contribution = float(input("Work retirement contribution %: "))
                user_obj.match = float(input("Employer match %: "))
                user_obj.personal_contribution = float(input("Percentage of monthly savings to personal retirement: "))
                user_obj.rate_return = float(input("Estimated investment rate of return (e.g., 0.07): ")) 
                user_obj.state = float(input("State tax %: "))
                user_obj.federal = float(input("Federal tax %: "))
                user_obj.savings = float(input("Monthly savings goal %: "))
                print("\nProfile successfully updated!")
            except ValueError:
                print("\nError: Please enter numbers only for financial data.")

    class Calculations:
        @classmethod
        def display_results(cls, user):
            # 1. Setup Variables for the Loop
            years_to_retire = user.retirement_age - user.age
            current_salary = user.salary
            tax_rate = user.state + user.federal
            
            total_work_retirement = 0.0
            total_personal_retirement = 0.0
            total_liquid_savings = 0.0

            # 2. Yearly Simulation (Accounts for Salary Raises)
            for year in range(years_to_retire):
                # Annual totals based on CURRENT year's salary
                yearly_net = current_salary * (1 - tax_rate)
                
                # Monthly breakdowns
                monthly_gross = current_salary / 12
                monthly_net = yearly_net / 12
                
                # Contributions (These grow as the salary grows)
                work_contrib_monthly = monthly_gross * (user.contribution + user.match)
                total_savings_monthly = monthly_net * user.savings
                
                personal_invest_monthly = total_savings_monthly * user.personal_contribution
                liquid_savings_monthly = total_savings_monthly - personal_invest_monthly

                # Apply growth to balances (Monthly compounding)
                for month in range(12):
                    # Work Retirement growth (assuming same rate of return as personal)
                    total_work_retirement = (total_work_retirement + work_contrib_monthly) * (1 + (user.rate_return / 12))
                    # Personal Retirement growth
                    total_personal_retirement = (total_personal_retirement + personal_invest_monthly) * (1 + (user.rate_return / 12))
                    # Liquid savings (assumed no interest/checking account)
                    total_liquid_savings += liquid_savings_monthly

                # Apply annual raise for the NEXT year
                current_salary *= (1 + user.annual_raise)

            # 3. Display Output
            print("\n" + "="*55)
            print(f"PROJECTION AT AGE {user.retirement_age} ({years_to_retire} YEARS FROM NOW)")
            print("="*55)
            print(f"Final Career Salary:         ${current_salary:,.2f}")
            print(f" (With {user.annual_raise*100:.1f}% annual raises)")
            print("-" * 55)
            
            print(f"Work Retirement Balance:     ${total_work_retirement:,.2f}")
            print(f"Personal Retirement Balance: ${total_personal_retirement:,.2f}")
            print("-" * 55)
            print(f"COMBINED NEST EGG:           ${(total_work_retirement + total_personal_retirement):,.2f}")
            print("-" * 55)
            print(f"Cash/Liquid Savings:         ${total_liquid_savings:,.2f}")
            print(f" (Savings not invested in retirement)")
            print("="*55)

# --- Execution Flow ---
new_account = Save_a_buck.Questions.create_new_user()
Save_a_buck.Questions.complete_profile(new_account)
Save_a_buck.Calculations.display_results(new_account)