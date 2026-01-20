import random

word_list = [
    "apple",  # 5
    "water",  # 5
    "phone",  # 5
    "table",  # 5
]

stages = [
    """
    
    
    
    
    
    
    ========
    """,
    """
      |
      |
      |
      |
      |
    ========
    """,
    """
  +---+
      |
      |
      |
      |
    ========
    """,
    """
  +---+
  |   |
      |
      |
      |
    ========
    """,
    """
  +---+
  |   |
  O   |
      |
      |
    ========
    """,
    """
  +---+
  |   |
  O   |
  |   |
      |
    ========
    """,
    """
  +---+
  |   |
  O   |
 /|   |
      |
    ========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
    ========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
    ========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
    ========
    """,
]

print(stages[0])

word = random.choice(word_list)
print(word)

placeholder = []

for i in range(1, len(word) + 1):
    placeholder.append("_")
print(placeholder)
current_stage = 0
won = False
for i in range(0, 15):
    if "_" in placeholder:
        alpha = input("Enter an alphabet\n:")
        found = False
        for i in range(0, len(word)):
            if word[i] == alpha:
                # print("Right")
                placeholder[i] = alpha
                found = True
        if not found:
            print("❌ Wrong Guess")
            current_stage += 1
            print(stages[current_stage])

            if current_stage == 9:
                print("You're Loose 😔😔")
        else:
            print("✅ Correct Guess")

        print(placeholder)
    else:
        won = True

if won:
    print("\n You're Won!!🎉🎉")
