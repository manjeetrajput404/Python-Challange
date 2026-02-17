# ================================
# NUMBER GUESSING GAME (Day 12)
# ================================

# 📌 New Learning in This Project:
# 1. How to use random module
# 2. How to control loops using a counter (attempts)
# 3. Using break to exit a loop early
# 4. Handling user input properly
# 5. Writing clean conditional logic

import random  # Used to generate a random number

# 🎯 Step 1: Generate a random number between 1 and 100
# randint(a, b) includes both a and b
result = random.randint(1, 100)

# 🎮 Welcome Messages
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# 🎚 Step 2: Set Difficulty Level
# .lower() prevents case sensitivity issues (Easy, EASY, easy all work)
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# 📌 Assign attempts based on difficulty
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    # 🚨 If user enters invalid input, exit program safely
    print("Invalid input!!!")
    exit()

# 🔁 Step 3: Game Loop
# Loop runs until attempts become 0
while attempts > 0:

    # 💡 UX Tip: Always show remaining attempts
    print(f"\nYou have {attempts} attempts remaining.")

    # Convert input to integer
    guess = int(input("Make a guess: "))

    # 🧠 Core Comparison Logic
    # Order matters: check greater, smaller, then equal
    if guess > result:
        print("Too High.")
    elif guess < result:
        print("Too Low.")
    else:
        # If not greater and not smaller → must be correct
        print(f"You got it! The answer was {result}")

        # 🔥 break stops the loop immediately
        # Without break, the game would continue even after winning
        break

    # ⚠ IMPORTANT:
    # Attempts should decrease ONLY if guess was wrong.
    # That’s why this line is placed AFTER the comparison.
    attempts -= 1


# 🏁 Step 4: Losing Condition
# If loop ends naturally (no break), attempts will be 0
if attempts == 0:
    print(f"You've run out of guesses. The number was {result}")


# ==========================================
# 🚨 COMMON MISTAKES YOU MIGHT MAKE:
# ==========================================

# ❌ Forgetting break → Game continues after winning
# ❌ Writing attempts -= 1 before checking guess
# ❌ Not handling invalid difficulty input
# ❌ Forgetting to convert input to int
# ❌ Using while attempts != 0 instead of while attempts > 0


# ==========================================
# 💡 TIPS & TRICKS
# ==========================================

# ✔ Use else instead of "elif guess == result" for cleaner code
# ✔ Always think about edge cases:
#     - What if user wins on last attempt?
#     - What if user enters wrong difficulty?
# ✔ Keep user experience in mind (show attempts)
# ✔ Think about loop exit conditions clearly


# ==========================================
# 🎓 INTERVIEW CONCEPTS USED HERE:
# ==========================================

# ✔ Loop control using counters
# ✔ Break statement
# ✔ Conditional branching
# ✔ Basic input validation
# ✔ Random number generation
