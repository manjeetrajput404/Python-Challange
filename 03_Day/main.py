# Example 1
temperature = 30

if temperature > 25:
    print("It's a sunny day")


# Example 2
age = 19

if age > 18:
    print("Congrats, You can eligible")
else :
    print("Sorry, You're not eligible")


# Example 3
number = 8

if number % 2 == 0:
    print(f"{number} is an Even number")
else:
    print(f"{number} is an Odd number")



# Example 4
score = 96
grade = None

if score>=50 and score<70:
    grade = "C"
elif score>=70 and score<85:
    grade = "B"
elif score>=85 and score<95:
    grade = "A"
elif score>=95 and score<=100:
    grade = "A+"

print(f"Your score is {score} and you have got the {grade} grade")
