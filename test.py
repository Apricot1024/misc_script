import numpy as np

def calculate_investment(weeks, weekly_investment=30, annual_rate=0.04, fee_rate=0.0008):
    daily_rate = 0.04/252  # 252 trading days in a year
    total_days = weeks * 5  # 5 trading days in a week
    investment = 0

    for day in range(weeks):
        investment += weekly_investment  # Invest weekly amount divided by 5 days
        investment *= (1 + daily_rate*5)  # Apply daily interest rate
        investment -= weekly_investment * fee_rate  # Subtract transaction fee

    return investment

weeks = 52  # Example: 52 weeks (1 year)
final_amount = calculate_investment(weeks)
print(f"Final amount after {weeks} weeks: {final_amount:.2f} CNY")