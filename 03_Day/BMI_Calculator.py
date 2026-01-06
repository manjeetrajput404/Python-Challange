height = 1.75  # in meters
weight = 70  # in kilograms

BMI = weight / (height * height)

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal")
elif BMI >= 25 and BMI <= 29.9:
    print("Overweight")
elif BMI >= 30:
    print("Obese")
