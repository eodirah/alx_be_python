#prompt the user to enter there income and expenses

monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

#calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

#using 5% annual interest rate to calculate projected savings

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#output result 
print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is : {projected_savings}.")
