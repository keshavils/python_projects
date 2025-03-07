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
computer_choice = ["Rock", "Paper", "Scissors"]
random_choice = ""

if sign == 0:
    print(rock)
    print("Compuer Choice: ")
    random_choice = random.choice(computer_choice)
    if random_choice == "Paper":
        print(paper, end="\n")
        print("You Lose!")
    elif random_choice == "Rock":
        print(rock, end="\n")
        print("It's Draw!")
    else:
        print(scissors, end="\n")
        print("You Win!")
elif sign == 1:
    print("Paper")
    print("Compuer Choice: ")
    random_choice = random.choice(computer_choice)
    if random_choice == "Scissors":
        print(scissors, end="\n")
        print("You Lose!")
    elif random_choice == "Paper":
        print(paper, end="\n")
        print("It's Draw!")
    else:
        print(rock, end="\n")
        print("You Win!")
elif sign == 2:
    print("Scissors")
    print("Compuer Choice: ")
    random_choice = random.choice(computer_choice)
    if random_choice == "Rock":
        print(rock, end="\n")
        print("You Lose!")
    elif random_choice == "Scissors":
        print(scissors, end="\n")
        print("It's Draw!")
    else:
        print(paper, end="\n")
        print("You Win!")
else:
    print("Wrong choose is given. You Lose!")
