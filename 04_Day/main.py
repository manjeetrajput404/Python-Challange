import random

Buddies = ["Abhay","Kunal","Deepanshu","Manjeet","Ravi","Rahul"]

randnum = random.randint(0,5)

print(f"{Buddies[randnum]} will pay the bill")
print(f"{random.choice(Buddies)} will pay the bill")