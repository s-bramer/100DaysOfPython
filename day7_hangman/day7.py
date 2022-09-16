import random

from replit import clear

import day7_art
import day7_words

# variables
word_list = day7_words.word_list
stages = day7_art.stages
logo = day7_art.logo
chosen_word = random.choice(word_list)
solution = []
guesses = []
game_over = False
lifes = 6

print(logo)

# prepare empty list and print it
for x in range(len(chosen_word)):
    solution.append("_")
print(f"{' '.join(solution)}")

# game loop
while not game_over:
    hits = 0
    guess = input("Please guess a letter: ").lower()
    clear()
    if guess not in chosen_word:
        lifes -= 1
        print(f"Sorry, '{guess}' is not in the word. You lose a life.")
        if lifes == 0:
            game_over = True
            print(
                f"GAME OVER. You've lost all your lifes! The word was '{chosen_word}'."
            )
    else:
        for x, letter in enumerate(chosen_word):
            if letter == guess:
                solution[x] = " " + guess + " "
                hits += 1
        print(f"YES, '{guess}' is in the word {hits} time(s).")

    # flag if user has already guessed this letter
    if guess in guesses:
        print(f"(You have guessed '{guess}' already.)")
    else:
        guesses.append(guess)

    # print current state of solution and lifes (hangman)
    print(f"{' '.join(solution)}")
    print(stages[lifes])

    # win conditon
    if "_" not in solution:
        game_over = True
        print("You WIN!!!")
