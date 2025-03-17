import random
from hangman_words import words_list
from hangman_art import *

print(logo[0])
chosen_word = random.choice(words_list).lower()
lives = 6
if lives == 6:
    print(stages[lives])


placeholder = "_"*len(chosen_word)
print(f"Guess the word: {placeholder}")
correct_letter = []

game_over = False

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in correct_letter:
        print(f"You've already guessed {guess}!")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # if guess in chosen_word:
    #     placeholder = display   
    #     print(display)
    #     if "_" in display:
    #         print(stages[lives])
    #         print(f"****************************{lives}/6 LIVES LEFT****************************")   

    if guess not in chosen_word:
        print(f"You guessed \"{guess}\", that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0: 
            game_over = True
            print(f"****************************IT WAS {chosen_word}! YOU LOSE****************************")
    
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN!****************************")

    print(stages[lives])
    
