# --------------------------------------
# Tip Calculator Program
# --------------------------------------

# Display welcome message
print("Welcome to the Tip Calculator!\n")

# Ask user for the total bill amount
total_bill = float(input("What was the total bill? ₹ "))

# Ask user for tip percentage
tip_percentage = float(input("How much tip would you like to give? (10, 12, or 15): "))

# Calculate the tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Calculate the total bill including tip
total_amount = total_bill + tip_amount

# Ask how many people to split the bill
total_people = int(input("How many people to split the bill? "))

# Calculate how much each person should pay
amount_per_person = total_amount / total_people

# Round the result to 2 decimal places
amount_per_person = round(amount_per_person, 2)

# Display the final result
print(f"\nEach person should pay: ₹ {amount_per_person}")
