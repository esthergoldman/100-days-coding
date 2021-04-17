height = int(input("What is your height?\n"))

bill =[]
if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >=45 and age <=55:
        bill = 0
        print("Please get your free ticket")
    else:
        bill = 12
        print("Please pay $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow")