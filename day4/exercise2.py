import random

names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")

chosen_one = random.randrange(0,len(names))
print(chosen_one)
winner = names[chosen_one]

print(f"{winner} is going to buy the meal today!")
