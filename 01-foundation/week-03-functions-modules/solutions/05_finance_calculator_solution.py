"""
Week 3 - Exercise 5: Finance Calculator (Solution)
Comprehensive financial calculator with multiple calculation types and validation.
"""

import math
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta
import json


class FinanceCalculator:
    """A comprehensive finance calculator class."""
    
    def __init__(self):
        self.calculation_history = []
    
    def compound_interest(self, principal: float, rate: float, time: float, 
                         compound_frequency: int = 1) -> Dict[str, float]:
        """
        Calculate compound interest.
        
        Args:
            principal (float): Initial investment amount
            rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
            time (float): Time period in years
            compound_frequency (int): Number of times interest compounds per year
            
        Returns:
            Dict[str, float]: Results including final amount, interest earned, etc.
        """
        self._validate_positive_values(principal=principal, rate=rate, time=time)
        if compound_frequency <= 0:
            raise ValueError("Compound frequency must be positive")
        
        # A = P(1 + r/n)^(nt)
        final_amount = principal * (1 + rate/compound_frequency) ** (compound_frequency * time)
        interest_earned = final_amount - principal
        
        result = {
            'principal': principal,
            'rate': rate,
            'time_years': time,
            'compound_frequency': compound_frequency,
            'final_amount': final_amount,
            'interest_earned': interest_earned,
            'total_return_percentage': (interest_earned / principal) * 100
        }
        
        self._add_to_history('compound_interest', result)
        return result
    
    def simple_interest(self, principal: float, rate: float, time: float) -> Dict[str, float]:
        """
        Calculate simple interest.
        
        Args:
            principal (float): Initial amount
            rate (float): Annual interest rate (as decimal)
            time (float): Time period in years
            
        Returns:
            Dict[str, float]: Results including interest and final amount
        """
        self._validate_positive_values(principal=principal, rate=rate, time=time)
        
        # I = P * r * t
        interest = principal * rate * time
        final_amount = principal + interest
        
        result = {
            'principal': principal,
            'rate': rate,
            'time_years': time,
            'interest_earned': interest,
            'final_amount': final_amount,
            'total_return_percentage': (interest / principal) * 100
        }
        
        self._add_to_history('simple_interest', result)
        return result
    
    def loan_payment(self, principal: float, rate: float, time: float, 
                    payment_frequency: int = 12) -> Dict[str, float]:
        """
        Calculate loan payment using the amortization formula.
        
        Args:
            principal (float): Loan amount
            rate (float): Annual interest rate (as decimal)
            time (float): Loan term in years
            payment_frequency (int): Number of payments per year (default 12 for monthly)
            
        Returns:
            Dict[str, float]: Payment information and totals
        """
        self._validate_positive_values(principal=principal, rate=rate, time=time)
        if payment_frequency <= 0:
            raise ValueError("Payment frequency must be positive")
        
        # Convert to payment period rate and number of payments
        period_rate = rate / payment_frequency
        num_payments = time * payment_frequency
        
        if rate == 0:
            # No interest case
            payment = principal / num_payments
            total_paid = principal
            total_interest = 0
        else:
            # M = P * [r(1+r)^n] / [(1+r)^n - 1]
            payment = principal * (period_rate * (1 + period_rate)**num_payments) / \
                     ((1 + period_rate)**num_payments - 1)
            total_paid = payment * num_payments
            total_interest = total_paid - principal
        
        result = {
            'loan_amount': principal,
            'annual_rate': rate,
            'loan_term_years': time,
            'payment_frequency': payment_frequency,
            'payment_amount': payment,
            'total_payments': int(num_payments),
            'total_paid': total_paid,
            'total_interest': total_interest,
            'interest_percentage': (total_interest / principal) * 100
        }
        
        self._add_to_history('loan_payment', result)
        return result
    
    def mortgage_calculator(self, home_price: float, down_payment: float, 
                          rate: float, term_years: int = 30) -> Dict[str, float]:
        """
        Calculate mortgage payments and related costs.
        
        Args:
            home_price (float): Total home price
            down_payment (float): Down payment amount
            rate (float): Annual interest rate (as decimal)
            term_years (int): Mortgage term in years
            
        Returns:
            Dict[str, float]: Comprehensive mortgage information
        """
        self._validate_positive_values(home_price=home_price, down_payment=down_payment, rate=rate)
        
        if down_payment >= home_price:
            raise ValueError("Down payment cannot be greater than or equal to home price")
        
        loan_amount = home_price - down_payment
        down_payment_percentage = (down_payment / home_price) * 100
        
        # Calculate monthly payment
        loan_info = self.loan_payment(loan_amount, rate, term_years, 12)
        
        # Additional mortgage costs (estimates)
        property_tax_annual = home_price * 0.0125  # 1.25% average
        insurance_annual = home_price * 0.0035     # 0.35% average
        pmi_annual = 0
        
        # PMI if down payment < 20%
        if down_payment_percentage < 20:
            pmi_annual = loan_amount * 0.005  # 0.5% of loan amount
        
        monthly_property_tax = property_tax_annual / 12
        monthly_insurance = insurance_annual / 12
        monthly_pmi = pmi_annual / 12
        
        total_monthly_payment = (loan_info['payment_amount'] + 
                               monthly_property_tax + 
                               monthly_insurance + 
                               monthly_pmi)
        
        result = {
            'home_price': home_price,
            'down_payment': down_payment,
            'down_payment_percentage': down_payment_percentage,
            'loan_amount': loan_amount,
            'annual_rate': rate,
            'term_years': term_years,
            'monthly_principal_interest': loan_info['payment_amount'],
            'monthly_property_tax': monthly_property_tax,
            'monthly_insurance': monthly_insurance,
            'monthly_pmi': monthly_pmi,
            'total_monthly_payment': total_monthly_payment,
            'total_interest_paid': loan_info['total_interest'],
            'total_cost_of_home': home_price + loan_info['total_interest']
        }
        
        self._add_to_history('mortgage_calculator', result)
        return result
    
    def retirement_savings(self, current_age: int, retirement_age: int, 
                          current_savings: float, monthly_contribution: float,
                          annual_return: float = 0.07) -> Dict[str, float]:
        """
        Calculate retirement savings projection.
        
        Args:
            current_age (int): Current age
            retirement_age (int): Planned retirement age
            current_savings (float): Current savings amount
            monthly_contribution (float): Monthly contribution amount
            annual_return (float): Expected annual return rate
            
        Returns:
            Dict[str, float]: Retirement savings projection
        """
        if current_age >= retirement_age:
            raise ValueError("Current age must be less than retirement age")
        if current_age < 0 or retirement_age < 0:
            raise ValueError("Ages must be non-negative")
        
        self._validate_positive_values(current_savings=current_savings, 
                                     monthly_contribution=monthly_contribution,
                                     annual_return=annual_return)
        
        years_to_retirement = retirement_age - current_age
        months_to_retirement = years_to_retirement * 12
        monthly_return = annual_return / 12
        
        # Future value of current savings
        future_value_current = current_savings * (1 + annual_return) ** years_to_retirement
        
        # Future value of monthly contributions (annuity)
        if monthly_return == 0:
            future_value_contributions = monthly_contribution * months_to_retirement
        else:
            future_value_contributions = monthly_contribution * \
                (((1 + monthly_return) ** months_to_retirement - 1) / monthly_return)
        
        total_retirement_savings = future_value_current + future_value_contributions
        total_contributions = monthly_contribution * months_to_retirement
        
        # Calculate potential monthly income in retirement (4% rule)
        monthly_retirement_income = total_retirement_savings * 0.04 / 12
        
        result = {
            'current_age': current_age,
            'retirement_age': retirement_age,
            'years_to_retirement': years_to_retirement,
            'current_savings': current_savings,
            'monthly_contribution': monthly_contribution,
            'annual_return_rate': annual_return,
            'total_contributions': total_contributions,
            'growth_from_current_savings': future_value_current - current_savings,
            'growth_from_contributions': future_value_contributions - total_contributions,
            'total_retirement_savings': total_retirement_savings,
            'estimated_monthly_income': monthly_retirement_income
        }
        
        self._add_to_history('retirement_savings', result)
        return result
    
    def investment_comparison(self, scenarios: List[Dict]) -> Dict[str, any]:
        """
        Compare multiple investment scenarios.
        
        Args:
            scenarios (List[Dict]): List of investment scenarios to compare
            
        Returns:
            Dict[str, any]: Comparison results
        """
        if not scenarios:
            raise ValueError("At least one scenario is required")
        
        results = []
        
        for i, scenario in enumerate(scenarios):
            name = scenario.get('name', f'Scenario {i+1}')
            
            # Calculate based on scenario type
            if scenario.get('type') == 'compound':
                result = self.compound_interest(
                    scenario['principal'],
                    scenario['rate'],
                    scenario['time'],
                    scenario.get('compound_frequency', 1)
                )
            elif scenario.get('type') == 'simple':
                result = self.simple_interest(
                    scenario['principal'],
                    scenario['rate'],
                    scenario['time']
                )
            else:
                # Default to compound interest
                result = self.compound_interest(
                    scenario['principal'],
                    scenario['rate'],
                    scenario['time'],
                    scenario.get('compound_frequency', 1)
                )
            
            results.append({
                'name': name,
                'scenario': scenario,
                'results': result
            })
        
        # Find best scenario
        best_scenario = max(results, key=lambda x: x['results']['final_amount'])
        
        comparison = {
            'scenarios': results,
            'best_scenario': best_scenario,
            'comparison_date': datetime.now().isoformat()
        }
        
        self._add_to_history('investment_comparison', comparison)
        return comparison
    
    def debt_payoff_calculator(self, debts: List[Dict], extra_payment: float = 0) -> Dict[str, any]:
        """
        Calculate debt payoff strategies (snowball vs avalanche).
        
        Args:
            debts (List[Dict]): List of debts with balance, rate, and minimum payment
            extra_payment (float): Extra amount to apply to debts
            
        Returns:
            Dict[str, any]: Payoff strategies comparison
        """
        if not debts:
            raise ValueError("At least one debt is required")
        
        # Validate debt data
        for debt in debts:
            if 'balance' not in debt or 'rate' not in debt or 'minimum_payment' not in debt:
                raise ValueError("Each debt must have balance, rate, and minimum_payment")
        
        # Snowball method (pay minimums + extra to lowest balance)
        snowball_debts = sorted(debts, key=lambda x: x['balance'])
        snowball_result = self._calculate_payoff_strategy(snowball_debts, extra_payment)
        
        # Avalanche method (pay minimums + extra to highest rate)
        avalanche_debts = sorted(debts, key=lambda x: x['rate'], reverse=True)
        avalanche_result = self._calculate_payoff_strategy(avalanche_debts, extra_payment)
        
        result = {
            'total_debt': sum(debt['balance'] for debt in debts),
            'total_minimum_payments': sum(debt['minimum_payment'] for debt in debts),
            'extra_payment': extra_payment,
            'snowball_method': snowball_result,
            'avalanche_method': avalanche_result,
            'recommended_method': 'avalanche' if avalanche_result['total_interest'] < snowball_result['total_interest'] else 'snowball'
        }
        
        self._add_to_history('debt_payoff', result)
        return result
    
    def _calculate_payoff_strategy(self, debts: List[Dict], extra_payment: float) -> Dict[str, any]:
        """Calculate debt payoff for a specific strategy."""
        debts_copy = [debt.copy() for debt in debts]
        total_interest = 0
        months = 0
        payoff_order = []
        
        while any(debt['balance'] > 0 for debt in debts_copy):
            months += 1
            remaining_extra = extra_payment
            
            # Pay minimums on all debts
            for debt in debts_copy:
                if debt['balance'] > 0:
                    monthly_interest = debt['balance'] * (debt['rate'] / 12)
                    total_interest += monthly_interest
                    
                    principal_payment = min(debt['minimum_payment'] - monthly_interest, debt['balance'])
                    debt['balance'] -= principal_payment
                    
                    if debt['balance'] <= 0:
                        debt['balance'] = 0
                        payoff_order.append({
                            'name': debt.get('name', 'Debt'),
                            'month': months
                        })
            
            # Apply extra payment to first debt with balance
            for debt in debts_copy:
                if debt['balance'] > 0 and remaining_extra > 0:
                    extra_principal = min(remaining_extra, debt['balance'])
                    debt['balance'] -= extra_principal
                    remaining_extra -= extra_principal
                    
                    if debt['balance'] <= 0:
                        debt['balance'] = 0
                        payoff_order.append({
                            'name': debt.get('name', 'Debt'),
                            'month': months
                        })
                    break
        
        return {
            'months_to_payoff': months,
            'years_to_payoff': months / 12,
            'total_interest': total_interest,
            'payoff_order': payoff_order
        }
    
    def _validate_positive_values(self, **kwargs):
        """Validate that all provided values are positive."""
        for name, value in kwargs.items():
            if value < 0:
                raise ValueError(f"{name.replace('_', ' ').title()} cannot be negative")
    
    def _add_to_history(self, calculation_type: str, result: Dict):
        """Add calculation to history."""
        self.calculation_history.append({
            'timestamp': datetime.now().isoformat(),
            'type': calculation_type,
            'result': result
        })
    
    def get_history(self) -> List[Dict]:
        """Get calculation history."""
        return self.calculation_history
    
    def clear_history(self):
        """Clear calculation history."""
        self.calculation_history.clear()
    
    def save_history(self, filename: str):
        """Save calculation history to file."""
        with open(filename, 'w') as f:
            json.dump(self.calculation_history, f, indent=2)
    
    def load_history(self, filename: str):
        """Load calculation history from file."""
        try:
            with open(filename, 'r') as f:
                self.calculation_history = json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found")
        except json.JSONDecodeError:
            print(f"Invalid JSON in file {filename}")


def format_currency(amount: float) -> str:
    """Format amount as currency."""
    return f"${amount:,.2f}"


def format_percentage(rate: float) -> str:
    """Format rate as percentage."""
    return f"{rate * 100:.2f}%"


def print_compound_interest_result(result: Dict):
    """Print compound interest results in a formatted way."""
    print(f"\n{'='*50}")
    print(f"COMPOUND INTEREST CALCULATION")
    print(f"{'='*50}")
    print(f"Principal Amount:      {format_currency(result['principal'])}")
    print(f"Annual Interest Rate:  {format_percentage(result['rate'])}")
    print(f"Time Period:           {result['time_years']} years")
    print(f"Compound Frequency:    {result['compound_frequency']} times per year")
    print(f"{'='*50}")
    print(f"Final Amount:          {format_currency(result['final_amount'])}")
    print(f"Interest Earned:       {format_currency(result['interest_earned'])}")
    print(f"Total Return:          {result['total_return_percentage']:.2f}%")


def print_loan_payment_result(result: Dict):
    """Print loan payment results in a formatted way."""
    print(f"\n{'='*50}")
    print(f"LOAN PAYMENT CALCULATION")
    print(f"{'='*50}")
    print(f"Loan Amount:           {format_currency(result['loan_amount'])}")
    print(f"Annual Interest Rate:  {format_percentage(result['annual_rate'])}")
    print(f"Loan Term:             {result['loan_term_years']} years")
    print(f"Payment Frequency:     {result['payment_frequency']} times per year")
    print(f"{'='*50}")
    print(f"Payment Amount:        {format_currency(result['payment_amount'])}")
    print(f"Total Payments:        {result['total_payments']}")
    print(f"Total Amount Paid:     {format_currency(result['total_paid'])}")
    print(f"Total Interest Paid:   {format_currency(result['total_interest'])}")


def print_mortgage_result(result: Dict):
    """Print mortgage calculation results in a formatted way."""
    print(f"\n{'='*50}")
    print(f"MORTGAGE CALCULATION")
    print(f"{'='*50}")
    print(f"Home Price:            {format_currency(result['home_price'])}")
    print(f"Down Payment:          {format_currency(result['down_payment'])} ({result['down_payment_percentage']:.1f}%)")
    print(f"Loan Amount:           {format_currency(result['loan_amount'])}")
    print(f"Interest Rate:         {format_percentage(result['annual_rate'])}")
    print(f"Term:                  {result['term_years']} years")
    print(f"{'='*50}")
    print(f"Principal & Interest:  {format_currency(result['monthly_principal_interest'])}")
    print(f"Property Tax:          {format_currency(result['monthly_property_tax'])}")
    print(f"Insurance:             {format_currency(result['monthly_insurance'])}")
    if result['monthly_pmi'] > 0:
        print(f"PMI:                   {format_currency(result['monthly_pmi'])}")
    print(f"Total Monthly Payment: {format_currency(result['total_monthly_payment'])}")
    print(f"Total Interest Paid:   {format_currency(result['total_interest_paid'])}")


def main():
    """Main function to run the finance calculator."""
    calculator = FinanceCalculator()
    
    print("💰 Welcome to the Finance Calculator!")
    
    while True:
        print(f"\n{'='*60}")
        print(f"FINANCE CALCULATOR MENU")
        print(f"{'='*60}")
        print("1. 📈 Compound Interest Calculator")
        print("2. 📉 Simple Interest Calculator")
        print("3. 🏠 Mortgage Calculator")
        print("4. 💳 Loan Payment Calculator")
        print("5. 🏖️ Retirement Savings Calculator")
        print("6. 📊 Investment Comparison")
        print("7. 💸 Debt Payoff Calculator")
        print("8. 📋 View Calculation History")
        print("9. 💾 Save/Load History")
        print("10. ❌ Exit")
        
        choice = input("\nSelect an option (1-10): ").strip()
        
        try:
            if choice == "1":
                print("\n📈 Compound Interest Calculator")
                principal = float(input("Enter principal amount: $"))
                rate = float(input("Enter annual interest rate (as decimal, e.g., 0.05 for 5%): "))
                time = float(input("Enter time period (years): "))
                frequency = int(input("Enter compound frequency per year (default 1): ") or "1")
                
                result = calculator.compound_interest(principal, rate, time, frequency)
                print_compound_interest_result(result)
            
            elif choice == "2":
                print("\n📉 Simple Interest Calculator")
                principal = float(input("Enter principal amount: $"))
                rate = float(input("Enter annual interest rate (as decimal): "))
                time = float(input("Enter time period (years): "))
                
                result = calculator.simple_interest(principal, rate, time)
                print(f"\nSimple Interest: {format_currency(result['interest_earned'])}")
                print(f"Final Amount: {format_currency(result['final_amount'])}")
            
            elif choice == "3":
                print("\n🏠 Mortgage Calculator")
                home_price = float(input("Enter home price: $"))
                down_payment = float(input("Enter down payment: $"))
                rate = float(input("Enter annual interest rate (as decimal): "))
                term = int(input("Enter loan term (years, default 30): ") or "30")
                
                result = calculator.mortgage_calculator(home_price, down_payment, rate, term)
                print_mortgage_result(result)
            
            elif choice == "4":
                print("\n💳 Loan Payment Calculator")
                principal = float(input("Enter loan amount: $"))
                rate = float(input("Enter annual interest rate (as decimal): "))
                time = float(input("Enter loan term (years): "))
                frequency = int(input("Enter payment frequency per year (default 12): ") or "12")
                
                result = calculator.loan_payment(principal, rate, time, frequency)
                print_loan_payment_result(result)
            
            elif choice == "5":
                print("\n🏖️ Retirement Savings Calculator")
                current_age = int(input("Enter current age: "))
                retirement_age = int(input("Enter retirement age: "))
                current_savings = float(input("Enter current savings: $"))
                monthly_contribution = float(input("Enter monthly contribution: $"))
                annual_return = float(input("Enter expected annual return (as decimal, default 0.07): ") or "0.07")
                
                result = calculator.retirement_savings(current_age, retirement_age, current_savings, 
                                                     monthly_contribution, annual_return)
                
                print(f"\nRetirement Projection:")
                print(f"Years to retirement: {result['years_to_retirement']}")
                print(f"Total contributions: {format_currency(result['total_contributions'])}")
                print(f"Total retirement savings: {format_currency(result['total_retirement_savings'])}")
                print(f"Estimated monthly income: {format_currency(result['estimated_monthly_income'])}")
            
            elif choice == "6":
                print("\n📊 Investment Comparison")
                scenarios = []
                
                num_scenarios = int(input("How many scenarios to compare? "))
                for i in range(num_scenarios):
                    print(f"\nScenario {i+1}:")
                    name = input("Enter scenario name: ")
                    principal = float(input("Enter principal: $"))
                    rate = float(input("Enter annual rate (as decimal): "))
                    time = float(input("Enter time (years): "))
                    
                    scenarios.append({
                        'name': name,
                        'principal': principal,
                        'rate': rate,
                        'time': time
                    })
                
                result = calculator.investment_comparison(scenarios)
                
                print(f"\n📊 Investment Comparison Results:")
                for scenario in result['scenarios']:
                    print(f"\n{scenario['name']}:")
                    print(f"  Final Amount: {format_currency(scenario['results']['final_amount'])}")
                    print(f"  Interest Earned: {format_currency(scenario['results']['interest_earned'])}")
                
                print(f"\n🏆 Best Scenario: {result['best_scenario']['name']}")
            
            elif choice == "7":
                print("\n💸 Debt Payoff Calculator")
                debts = []
                
                num_debts = int(input("How many debts? "))
                for i in range(num_debts):
                    print(f"\nDebt {i+1}:")
                    name = input("Enter debt name: ")
                    balance = float(input("Enter balance: $"))
                    rate = float(input("Enter annual interest rate (as decimal): "))
                    minimum_payment = float(input("Enter minimum payment: $"))
                    
                    debts.append({
                        'name': name,
                        'balance': balance,
                        'rate': rate,
                        'minimum_payment': minimum_payment
                    })
                
                extra_payment = float(input("Enter extra payment amount: $") or "0")
                
                result = calculator.debt_payoff_calculator(debts, extra_payment)
                
                print(f"\n💸 Debt Payoff Results:")
                print(f"Total Debt: {format_currency(result['total_debt'])}")
                print(f"Extra Payment: {format_currency(result['extra_payment'])}")
                print(f"\nSnowball Method: {result['snowball_method']['months_to_payoff']} months")
                print(f"Avalanche Method: {result['avalanche_method']['months_to_payoff']} months")
                print(f"Recommended: {result['recommended_method'].title()} Method")
            
            elif choice == "8":
                print("\n📋 Calculation History")
                history = calculator.get_history()
                if not history:
                    print("No calculations in history.")
                else:
                    for i, calc in enumerate(history[-10:], 1):  # Show last 10
                        print(f"{i}. {calc['type'].replace('_', ' ').title()} - {calc['timestamp'][:19]}")
            
            elif choice == "9":
                print("\n💾 Save/Load History")
                action = input("(S)ave or (L)oad history? ").lower().strip()
                filename = input("Enter filename: ")
                
                if action == 's':
                    calculator.save_history(filename)
                    print(f"History saved to {filename}")
                elif action == 'l':
                    calculator.load_history(filename)
                    print(f"History loaded from {filename}")
            
            elif choice == "10":
                print("💰 Thank you for using the Finance Calculator!")
                break
            
            else:
                print("❌ Invalid choice! Please select 1-10.")
        
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
