# main.py
from save_a_buck_calculations import Calculations

def main():
    print("=== Welcome to Save-A-Buck! ===\n")

    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    email_addr = input("Enter your email: ")

    # Use Calculations instead of Questions
    user_app = Calculations(fname, lname, email_addr)

    print(f"\n{user_app.user()}")
    print("-" * 30)

    # These methods still work because Calculations inherits from Questions
    user_app.ask_salary_questions()
    user_app.add_expenditures()
    user_app.show_spending_summary()
    
    # New calculation methods
    user_app.calculate_remaining_budget()
    
    print(f"\nFinancial profile complete for {email_addr}.")

if __name__ == "__main__":
    main()