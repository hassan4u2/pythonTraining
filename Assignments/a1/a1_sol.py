'''
# q1 

from math import log

x, y = [int(i) for i in input("Enter two numbers: ").split(" ")]

print(
    "\nx = ", x,
    "\ny = ", y,
    "\nx**y = ", x**y,
    "\nlog(x) = ", log(x, 2)
    )

'''


'''
# q2 part A solution

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0
rate = 0.04
months = 0

while current_savings < (total_cost * portion_down_payment):
    current_savings += (current_savings * rate / 12) + (annual_salary * portion_saved / 12)
    months += 1
    print("Current savings: ", current_savings , "Month: ", months)

print("Number of months: ", months)

'''




'''
# q2 part B solution

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment = 0.25
current_savings = 0
rate = 0.04
months = 0

while current_savings < (total_cost * portion_down_payment):
    current_savings += (current_savings * rate / 12) + (annual_salary * portion_saved / 12)
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        print("Current savings: ", current_savings , "Month: ", months)

print("Number of months: ", months)

'''