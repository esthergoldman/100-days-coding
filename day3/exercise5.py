print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

names = name1 + name2

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

true =  t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love = l + o + v + e

total = int(str(true) + str(love))


if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos")
elif total >= 40 and total <=50:
    print(f"Your score is {total}, you are alright together")
else:
    print(f"Your score is {total}")