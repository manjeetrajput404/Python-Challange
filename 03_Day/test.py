# Problem 1
# (WAP to check whether a number is odd or even)

number = int(input("Enter a Number \n"))

if number % 2 == 0:
    print("The number is an Even number")
else:
    print("The number is an Odd number")


# ________________________________________________________________________________________________________
# Problem 2

height = int(input("Enter your Height (in cm): "))
age = int(input("Enter your age: "))
want_photo = input("If you want to take photos press Y and if not press N: ").lower()

cost = 0

if height < 120:
    print("Can't ride")
else:
    print("Can ride")

    if age >= 45 and age <= 55:
        cost = 0
        print("Special offer! Everything is FREE 🎉")

    elif age < 12:
        cost = 5

    elif age <= 18:
        cost = 7

    else:
        cost = 12

    # Only add photo charge if NOT in free group
    if not (age >= 45 and age <= 55):
        if want_photo == "y":
            cost += 3

    print(f"Total cost is ${cost}")

# -----------------------------------------------------------
# Problem 3
# Pizza Delivery Program

print("Welcome to Python Pizza Deliverable 🍕\n")

size = input("What size of pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
want_extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

# Pizza pricing
small_pizza = 15
medium_pizza = 20
large_pizza = 25

# Pepperoni pricing
pep_sm_pizza = 2
pep_med_pizza = 3
pep_lar_pizza = 3

# Extra cheese price
extra_cheese_price = 1

cost = 0

if size == "s":
    cost = small_pizza
    if pepperoni == "y":
        cost += pep_sm_pizza

elif size == "m":
    cost = medium_pizza
    if pepperoni == "y":
        cost += pep_med_pizza

elif size == "l":
    cost = large_pizza
    if pepperoni == "y":
        cost += pep_lar_pizza

else:
    print("Invalid size selected!")
    exit()

if want_extra_cheese == "y":
    cost += extra_cheese_price

print(f"Your final pizza cost is ${cost}")
