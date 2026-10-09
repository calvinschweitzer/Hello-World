#Calvin Schweitzer
#09/10/2026
#Homework 1

#1, Sales tax calculator
item_price = float(input("What is the price of the item?"))
quantity = int(input("What quantity are you buying?"))

tax_rate = 0.075

subtotal = item_price * quantity
print("Your subtotal is:",subtotal,"$", round(subtotal,2))
tax_amount = subtotal * tax_rate
print("The tax amount is: ", tax_amount,"$", round(tax_amount,2))
total_cost = subtotal + tax_amount
print("Your total is: ", total_cost,"$", round(total_cost,2))

#2, Employee weekly pay calculator
hourly_wage = float(input("What is your hourly wage? "))
hours_worked = float(input("Hpw many hours did you work this week? "))

overtime_limit = 40
overtime_rate = 1.5

if hours_worked > overtime_limit:
    regular_hours = overtime_limit
    overtime_hours = hours_worked - overtime_limit
else:
    regular_hours = hours_worked
    overtime_hours = 0

base_pay = regular_hours * hourly_wage
overtime_pay = overtime_hours * hourly_wage  *overtime_rate
total_pay = base_pay + overtime_pay

print("Your base pay is: ", round(base_pay,2))
print("Your overtime pay is: ", round(overtime_pay,2))
print("Your total pay is: ", round(total_pay,2))

#3, Student grade calculator
numeric_grade = float(input("What is your numeric grade?"))

if numeric_grade >= 90:
    letter_grade = "A"
elif numeric_grade >= 80:
    letter_grade = "B"
elif numeric_grade >= 70:
    letter_grade = "C"
elif numeric_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
print("Your numeric grade is:", numeric_grade)
print("Your letter grade is: ", letter_grade)

#4, Bonus eligibility checker
hours_recorded = float(input("How many hours did you work? "))
performance_score = float(input("What is your performance score? "))

hours_required = 35
score_required = 85
bonus_amount = 100

if hours_recorded > hours_required and performance_score > score_required:
    print("Congratulations!, you are eligible for a bonus.")
    print("Your bonus is: $", round(bonus_amount,2))
else:
    hours_needed = hours_required - hours_worked
    points_needed = score_required - performance_score
    
    if hours_needed > 0:
        print("You need:", round(hours_needed,2),"more hours to qualify")
    if points_needed > 0:
        print("You need:", round(points_needed,2),"more points to qualify")

