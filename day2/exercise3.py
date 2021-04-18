#There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = (int(input("What is your current age?")))

days = 365 * 90 - 365 * age

weeks = 52 * 90 - 52 * age

months = 12 * 90 - 12 * age

print(f"You have {days} days, {weeks} weeks, and {months} months left.")