# Exercise 5: Personal Finance Calculator (Weekend Project)
# TODO: Create a comprehensive personal finance calculator using functions and modules

import datetime
import math

# Basic calculation functions
def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest"""
    # TODO: Formula: I = P * R * T / 100
    pass

def calculate_compound_interest(principal, rate, time, compound_frequency=1):
    """Calculate compound interest"""
    # TODO: Formula: A = P(1 + r/n)^(nt)
    # Where: P=principal, r=rate/100, n=compound_frequency, t=time
    pass

def calculate_loan_payment(principal, annual_rate, years):
    """Calculate monthly loan payment"""
    # TODO: Use the loan payment formula
    # M = P * [r(1+r)^n] / [(1+r)^n - 1]
    # Where: M=monthly payment, P=principal, r=monthly rate, n=number of payments
    pass

def calculate_savings_goal(goal_amount, monthly_deposit, annual_rate):
    """Calculate time needed to reach savings goal"""
    # TODO: Calculate months needed to reach goal with compound interest
    pass

# Investment functions
def calculate_future_value(present_value, annual_rate, years):
    """Calculate future value of investment"""
    # TODO: FV = PV * (1 + r)^t
    pass

def calculate_break_even(fixed_costs, price_per_unit, variable_cost_per_unit):
    """Calculate break-even point"""
    # TODO: Break-even = Fixed Costs / (Price - Variable Cost)
    pass

def calculate_roi(gain, cost):
    """Calculate Return on Investment"""
    # TODO: ROI = (Gain - Cost) / Cost * 100
    pass

# Budget analysis functions
def analyze_budget(income, expenses_dict):
    """
    Analyze monthly budget
    
    Args:
        income: Monthly income
        expenses_dict: Dictionary of expense categories and amounts
    
    Returns:
        dict: Budget analysis with recommendations
    """
    # TODO: Calculate total expenses, savings, percentages
    # Provide recommendations based on 50/30/20 rule
    pass

def calculate_debt_payoff(debt_amount, interest_rate, monthly_payment):
    """Calculate debt payoff timeline"""
    # TODO: Calculate months to pay off debt and total interest paid
    pass

def calculate_emergency_fund(monthly_expenses, months_coverage=6):
    """Calculate recommended emergency fund"""
    # TODO: Recommend emergency fund size
    pass

# Retirement planning functions
def calculate_retirement_savings(current_age, retirement_age, current_savings, 
                               monthly_contribution, annual_return):
    """Calculate retirement savings projection"""
    # TODO: Project retirement savings based on current savings and contributions
    pass

def calculate_401k_match(salary, contribution_percent, match_percent, match_limit):
    """Calculate 401(k) employer match"""
    # TODO: Calculate employer matching contribution
    pass

# Tax calculation functions  
def calculate_tax_bracket(income, tax_brackets):
    """Calculate tax owed based on progressive tax brackets"""
    # TODO: Implement progressive tax calculation
    # tax_brackets should be list of (min_income, max_income, rate) tuples
    pass

def calculate_after_tax_income(gross_income, tax_rate, deductions=0):
    """Calculate take-home pay"""
    # TODO: Calculate net income after taxes and deductions
    pass

# Utility functions
def format_currency(amount):
    """Format number as currency"""
    # TODO: Format as currency with commas and dollar sign
    pass

def get_current_date():
    """Get current date information"""
    # TODO: Return current date, year, month for calculations
    pass

def create_financial_report(name, calculations):
    """Create a formatted financial report"""
    # TODO: Create a nice formatted report with all calculations
    pass

# Main menu function
def main_menu():
    """Main menu for the finance calculator"""
    print("="*50)
    print("       PERSONAL FINANCE CALCULATOR")
    print("="*50)
    
    while True:
        print("\n💰 Choose a calculation:")
        print("1. 📈 Interest Calculations")
        print("2. 🏠 Loan Calculator")
        print("3. 💼 Investment Analysis")
        print("4. 📊 Budget Analysis")
        print("5. 🏖️  Retirement Planning")
        print("6. 💸 Tax Calculations")
        print("7. 📋 Generate Report")
        print("8. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        # TODO: Implement menu handling
        # Call appropriate functions based on user choice
        
        if choice == '8':
            print("Thank you for using the Personal Finance Calculator!")
            break

# Test functions
def run_tests():
    """Test all calculator functions"""
    print("Running finance calculator tests...")
    
    # TODO: Test all your functions with sample data
    # Example tests:
    # print(f"Simple interest: ${calculate_simple_interest(1000, 5, 2)}")
    # print(f"Compound interest: ${calculate_compound_interest(1000, 5, 2, 12)}")
    # etc.

if __name__ == "__main__":
    # Uncomment to run tests first
    # run_tests()
    
    # Start the main program
    main_menu()
