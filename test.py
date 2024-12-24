import numpy as np
import matplotlib.pyplot as plt


weeks = 52*3  # Example: 52 weeks (1 year)



weeks_list = range(1, weeks+1)
def calculate_investment(weeks, weekly_investment=80, annual_rate=0.04, fee_rate=0.001):
    daily_rate = annual_rate/252  # 252 trading days in a year
    investment = 1120

    for week in range(weeks):
        if week >= 52*3:
            weekly_investment = 120
        if week >= 52*6:
            weekly_investment = 300
        investment += weekly_investment  # Invest weekly amount
        investment *= (1 + daily_rate*5)  # Apply daily interest rate
        investment -= weekly_investment * fee_rate  # Subtract transaction fee

    return investment

amounts = [calculate_investment(week) for week in weeks_list]
print(f"Final amount after {weeks} weeks: {amounts[-1]:.2f} CNY")

plt.plot(weeks_list, amounts)
plt.xlabel('Weeks')
plt.ylabel('Total Amount (CNY)')
plt.title('Total Amount vs Weeks')
plt.grid(True)
plt.show()