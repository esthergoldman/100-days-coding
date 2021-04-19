import random
#rock paper scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


question = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

compu = random.randint(0,2)

print(compu)


if question == 0 and compu == 0:
    print(f"{rock}\n{rock}\nIt's a draw")
elif question == 0 and compu == 1:
    print(f"{rock}\nComputer chose:\n{paper}\n GAME OVER :(")
elif question == 0 and compu == 2:
    print(f"{rock}\nComputer chose:\n{scissors}\n WELL DONE :) ")
elif question == 1 and compu == 0:
    print(f"{paper}\nComputer chose:\n{rock}\n WELL DONE :)")
elif question == 1 and compu == 1:
    print(f"{paper}\n {paper}\nIt's a draw")
elif question == 1 and compu == 2:
    print(f"{paper}\nComputer chose:\n{scissors}\nGAME OVER :( ")
elif question == 2 and compu == 2:
    print(f"{scissors}\nComputer chose:\n{scissors}\nIt's a draw")
elif question == 2 and compu == 0:
    print(f"{scissors}\nComputer chose:\n{rock}\nGAME OVER ")
elif question == 2 and compu == 1:
    print(f"{scissors}\nComputer chose:\n{paper}\nWELL DONE :)")

else:
    print("Sorry try again")