import random

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

#Write your code below this line 👇
rpc = [rock,paper,scissors]
cpu_choice = random.randint(0,2)
my_choice = int(input("Choose Rock (0), Paper (1) or Scissors (2): "))
print(f"Your choice:\n{rpc[my_choice]}\nComputer choose:\n{rpc[cpu_choice]}")

if cpu_choice == my_choice:
     print("Its a draw.")
else:
    if cpu_choice == 0 and my_choice == 1:
        print("You win.")
    elif cpu_choice == 1 and my_choice == 2:
        print("You win.")
    elif cpu_choice == 2 and my_choice == 0:
        print("You win.")
    else:
        print("You lose.")
