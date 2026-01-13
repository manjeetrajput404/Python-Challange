cost = None
height = int(input("Enter your Height in cm : \n"))

if height <= 120:
    print("Can't ride")
else:
    print("Can ride")

    age = int(input("Enter your age: \n"))

    if age > 45 and age < 55:
        cost = 0
    elif age <= 12:
        cost = 5
    elif age > 12 and age < 18:
        cost = 7
    elif age >= 18:
        cost = 12

    wantPhotos = input("Do you want photos, Press Y or N").lower()

    if wantPhotos == "y":
        cost += 3

    print(f"Your total bill is ${cost}")
