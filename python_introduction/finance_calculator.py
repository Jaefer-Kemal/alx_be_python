income = int(input("Enter your monthly income: "))
total_expense = int(input("Enter your total monthly expenses: "))

monthly_savings =  income - total_expense
print(f"Your monthly savings are ${monthly_savings}.")

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Projected savings after one year, with interest, is: ${round(projected_savings)}.")