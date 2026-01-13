import random #inbuilt module
# import myModule #custom module

# print(myModule.number) # custom module variable

# random_number = random.randint(1,6)
# print(random_number)

# ---------------------------------------------------------------------
# Method 1

# randomNumber = random.random() * 2
# randnum = round(randomNumber,0)

# if randnum == 1:
#     print("Heads")
# else:
#     print("Tails")
# ____________________________________
# Method 2

# randnum = random.randint(1,2)
# if randnum == 1:
#     print("Heads")
# else:
#     print("Tails")

# ______________________________________
# Method 3
print(random.choice(["Heads","Tails"]))



