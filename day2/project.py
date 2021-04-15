#tip calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
bill= float(input("What was the total bill?\n"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to slip the bill?\n"))


choose_percentage = bill * (percentage / 100)
new_total = bill + choose_percentage
total= round(new_total / people,2)
print(f"Each person should pay: ${total}")

