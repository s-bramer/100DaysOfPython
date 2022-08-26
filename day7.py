import random

word_list = ["aardvark", "baboon", "camel"]

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

# variables
chosen_word = random.choice(word_list)
solution = []
game_over = False
lifes = 6

print(chosen_word)

for x in range(len(chosen_word)):
    solution.append("_")
print(solution)

# game loop
while not game_over:
    guess = input("Please guess a letter: ").lower()
    if guess not in chosen_word:
        lifes -= 1
    else:
        for x, letter in enumerate(chosen_word):
            if letter == guess:
                solution[x] = " " + guess + " "
    print(solution)
    print(stages[lifes])
    if lifes == 0:
        print("You lose!")
        break
    if "_" not in solution:
        game_over = True
        print("You WIN!!!")
