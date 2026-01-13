print("Welcome to Treseure Island. \n Your mission is to find the treasure.\n")

level1 = input("left or right? \n").lower()
if level1 == "right":
    print("Game Over")
else:
    level2 = input("Wait or swim \n").lower()
    if level2 == "swim":
        print("Game Over")
    else:
        level3 = input("Which door? Blue, Yellow and Red \n").lower()
        if level3 == "red" or level3 == "blue":
            print("Game Over")
        else:
            print("You win!")
