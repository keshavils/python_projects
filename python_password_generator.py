import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '(', ')', '*', '+', '&']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

print("\n")
strong_password = []
hard_level_password = ""
easy_level_password = ""


#Easy Level
for char in range(nr_letters):
    easy_level_password += random.choice(letters)
    strong_password.append(random.choice(letters))

for char in range(nr_symbols):
    easy_level_password += random.choice(symbols)
    strong_password.append(random.choice(symbols))

for char in range(nr_numbers):
    easy_level_password += random.choice(numbers)
    strong_password.append(random.choice(numbers))

print("Here is your easy level password: " + easy_level_password)

#Hard Level
random.shuffle(strong_password)

for f in strong_password:
    hard_level_password += f

print("Here is your hard level password: " + hard_level_password)
