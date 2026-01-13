# ____________________________________________________________________________________________________
# My Code
# ____________________________________________________________________________________________________

import random

print("-------------------------------------------------- ")
print("Welcome to the Rock , Paper and Scissors Game🥳 ")
print("-------------------------------------------------- ")


ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_score = 0
computer_score = 0

user_choice = int(input(
"""Press 1 for Rock
Press 2 for Paper
Press 3 for Scissors 
""")
)

computer_choice = random.choice(["Rock", "Paper", "Scissors"])
print("Computer Choice is", computer_choice)

# ----------------------------------------------------
# 1 Rock

if user_choice == 1 and computer_choice == "Rock":
    print(f"You're Choose: \n {ROCK}")
    print(f"Computer choice is: \n {ROCK}")
    print("Rock ,Game tie !")

elif user_choice == 1 and computer_choice == "Paper":
    print(f"You're Choose: \n {ROCK}")
    print(f"Computer choice is: \n {PAPER}")
    print("You're lose !")
    computer_score += 1

elif user_choice == 1 and computer_choice == "Scissors":
    print(f"You're Choose: \n {ROCK}")
    print(f"Computer choice is: \n {SCISSORS}")
    print("You're Won !")
    user_score += 1

# 2 Paper

elif user_choice == 2 and computer_choice == "Rock":
    print(f"You're Choose: \n {PAPER}")
    print(f"Computer choice is: \n {ROCK}")
    print("You're won !")
    user_score += 1

elif user_choice == 2 and computer_choice == "Paper":
    print(f"You're Choose: \n {PAPER}")
    print(f"Computer choice is: \n {PAPER}")
    print("Game tie !")

elif user_choice == 2 and computer_choice == "Scissors":
    print(f"You're Choose: \n {PAPER}")
    print(f"Computer choice is: \n {SCISSORS}")
    print("You're lose !")
    computer_score += 1


# 3 scissors

elif user_choice == 3 and computer_choice == "Rock":
    print(f"You're Choose: \n {SCISSORS}")
    print(f"Computer choice is: \n {ROCK}")
    print("You're lose !")
    computer_score += 1

elif user_choice == 3 and computer_choice == "Paper":
    print(f"You're Choose: \n {SCISSORS}")
    print(f"Computer choice is: \n {PAPER}")
    print("You're won !")
    user_score += 1

elif user_choice == 3 and computer_choice == "Scissors":
    print(f"You're Choose: \n {SCISSORS}")
    print(f"Computer choice is: \n {SCISSORS}")
    print("Game tie !")


print(f"Your score is {user_score} and Computer Score is: {computer_score}")



# _________________________________________________________________________________________________________
# Improvement version
# _________________________________________________________________________________________________________

import random

print("-------------------------------------------------- ")
print("Welcome to the Rock , Paper and Scissors Game 🥳")
print("-------------------------------------------------- ")

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

arts = [ROCK, PAPER, SCISSORS]
names = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

user_choice = int(input(
"""Press 1 for Rock
Press 2 for Paper
Press 3 for Scissors
"""))

if user_choice < 1 or user_choice > 3:
    print("❌ Invalid choice! You lose.")
else:
    user_index = user_choice - 1
    computer_index = random.randint(0, 2)

    print("You chose:")
    print(arts[user_index])

    print("Computer chose:")
    print(arts[computer_index])

    if user_index == computer_index:
        print("🤝 It's a tie!")

    elif (user_index == 0 and computer_index == 2) or \
         (user_index == 1 and computer_index == 0) or \
         (user_index == 2 and computer_index == 1):
        print("🎉 You won!")
        user_score += 1
    else:
        print("💀 You lost!")
        computer_score += 1

print(f"Your score: {user_score} | Computer score: {computer_score}")
