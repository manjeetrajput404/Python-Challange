import random

def ace_cheking(member,number):
    if score["member"] < 10:
        return 11
    else:
        return 1

cards = {0,2,3,4,5,6,7,8,9,10,10,10,10}

score = {
    "user": 0,
    "computer": 0
}

shuffle = 2

while not shuffle == 0:
    score["user"] += random.choice(cards)
    score["computer"] += random.choice(cards)
    shuffle -= 1

    if score["user"] > 15 and score["user"] < 21:
        if score["user"] == score["computer"]:
            print("The game is tie!!")

        elif score["user"] > score["computer"]:
            print(f"Your score is {score["user"]}, and you win")
    
    elif score["computer"] > 15 and score["computer"] < 21:
        if score["computer"] > score["user"]:
            print(f"Computer score is {score["computer"]}, and they're win")

    new_card = input("Do you need a New Card, Y or N").lower()
    if new_card == 'y':
        score += 1