import os
import random
import project_items


print(os.name)
def clearScreen():
    "cls" if os == "nt" else "clear"
for i in range(0, 5):
    person1 = random.choice(project_items.persons)
    person2 = random.choice(project_items.persons)
    print(f"Person1 : {person1['name']}\nPerson2 : {person2['name']}")

    guess = int(input("which Player have hiighest Followers, Press 1 or 2"))
    if guess == 1 and person1["followers"] > person2["followers"]:
        print("Right Guess !")
        print(
            f"{person1['name']} followers is {person1['followers']}\n{person2['name']} followers is {person2['followers']}"
        )
    elif guess == 2 and person1["followers"] < person2["followers"]:
        print(
            f"{person1['name']} followers is {person1['followers']}\n{person2['name']} followers is {person2['followers']}"
        )
        print("Right Guess")
    else:
        print("Wrong Guess or Invalid !!")
        break

print("Thanks for playing, Visit again")
