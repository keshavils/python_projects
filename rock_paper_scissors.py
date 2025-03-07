import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

sign = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if sign == 0:
    print(rock)
    print("Compuer Choice: ")
    if computer_choice == 1:
        print(paper, end="\n")
        print("You Lose!")
    elif computer_choice == 0:
        print(rock, end="\n")
        print("It's Draw!")
    else:
        print(scissors, end="\n")
        print("You Win!")
elif sign == 1:
    print("Paper")
    print("Compuer Choice: ")
    if computer_choice == 2:
        print(scissors, end="\n")
        print("You Lose!")
    elif computer_choice == 1:
        print(paper, end="\n")
        print("It's Draw!")
    else:
        print(rock, end="\n")
        print("You Win!")
elif sign == 2:
    print("Scissors")
    print("Compuer Choice: ")
    if computer_choice == 0:
        print(rock, end="\n")
        print("You Lose!")
    elif computer_choice == 2:
        print(scissors, end="\n")
        print("It's Draw!")
    else:
        print(paper, end="\n")
        print("You Win!")
else:
    print("You typed an invalid number. You Lose!")
