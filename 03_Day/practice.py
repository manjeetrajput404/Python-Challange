# 🟢 Level 1

# Take a number and check if it is positive or negative
number = 5

if number<1:
    print(f"The number {number} is an negative number")
elif number>=1:
    print(f"The number {number} is an positive number")


# Check if a person is eligible to vote
age = 19

if age > 18:
    print("Congrats, You're eligible to vote")
elif age <= 18:
    print("Sorry, You're not elgible to vote")


# 🟡 Level 2

# Check if a number is even or odd
number = 54
 
if number % 2 == 0:
    print("It's an even number")
else:
    print("It's an Odd number")



# Print grades based on marks
score = 80
grade = None

if score>=70 and score<80:
    grade = "c"
elif score>=80 and score<90:
    grade = "B"
elif score>=90 and score<95:
    grade = "A"
elif score>=95 and score<=100:
    grade = "A++"

print(f"Your total score is {score} and you're got the {grade} grade")




