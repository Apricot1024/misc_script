import numpy as np

def calculate_investment(weeks, weekly_investment=60, annual_rate=0.04, fee_rate=0.001):
    daily_rate = annual_rate/252  # 252 trading days in a year
    investment = 1120

    for day in range(weeks):
        investment += weekly_investment  # Invest weekly amount divided by 5 days
        investment *= (1 + daily_rate*5)  # Apply daily interest rate
        investment -= weekly_investment * fee_rate  # Subtract transaction fee

    return investment

weeks = 52*60  # Example: 52 weeks (1 year)
final_amount = calculate_investment(weeks)
print(f"Final amount after {weeks} weeks: {final_amount:.2f} CNY")

import matplotlib.pyplot as plt

weeks_list = range(1, weeks+1)
amounts = [calculate_investment(weeks) for weeks in weeks_list]

plt.plot(weeks_list, amounts)
plt.xlabel('Weeks')
plt.ylabel('Total Amount (CNY)')
plt.title('Total Amount vs Weeks')
plt.grid(True)
plt.show()