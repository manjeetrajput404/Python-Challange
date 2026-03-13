# ==============================
# ☕ PYTHON COFFEE MACHINE
# ==============================

# ------------------------------
# FUNCTIONAL REQUIREMENTS:
# 1. User can order espresso, latte, cappuccino
# 2. Machine checks resource availability
# 3. Machine processes coins
# 4. Machine calculates profit
# 5. User can request report
# 6. User can turn off machine
# ------------------------------

# ------------------------------
# NON-FUNCTIONAL REQUIREMENTS:
# 1. Good user experience messages
# 2. No sudden program termination
# 3. Clean readable structure
# 4. Input validation
# 5. Modular function design
# ------------------------------

# Menu Data (Static Configuration)
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

# Available Resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


# ------------------------------
# Check if enough ingredients exist
# ------------------------------
def check_resources(drink, quantity):
    for item in MENU[drink]["ingredients"]:
        required_amount = MENU[drink]["ingredients"][item] * quantity
        if required_amount > resources[item]:
            print(f"❌ Sorry, not enough {item}.")
            return False
    return True


# ------------------------------
# Deduct ingredients after successful payment
# ------------------------------
def make_coffee(drink, quantity):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item] * quantity


# ------------------------------
# Process coins and calculate change
# ------------------------------
def process_payment(cost, quantity):
    global profit
    print("\n💰 Please insert coins.")

    try:
        penny = int(input("How many pennies? "))
        dime = int(input("How many dimes? "))
        nickel = int(input("How many nickels? "))
        quarter = int(input("How many quarters? "))
    except ValueError:
        print("⚠ Invalid input. Please enter numbers only.")
        return None

    total = (penny * 0.01) + (dime * 0.10) + (nickel * 0.05) + (quarter * 0.25)
    bill = cost * quantity

    if total < bill:
        print("❌ Sorry, that's not enough money. Money refunded.")
        return None

    change = round(total - bill, 2)
    profit += bill
    return change


# ------------------------------
# Display machine report
# ------------------------------
def report():
    print("\n📊 Machine Report:")
    for key, value in resources.items():
        print(f"{key.capitalize()}: {value}")
    print(f"Profit: ${profit}")
    print("-" * 25)


# ==============================
# MAIN PROGRAM LOOP
# ==============================

print("☕ Welcome to Python Coffee Machine!")
print("Available drinks: espresso ($1.5), latte ($2.5), cappuccino ($3.0)")
print("Type 'report' to see machine status.")
print("Type 'off' to turn off the machine.\n")

machine_on = True

while machine_on:
    user_input = input("What would you like? ").lower()

    if user_input == "off":
        print("🔴 Turning off machine. Goodbye!")
        machine_on = False

    elif user_input == "report":
        report()

    elif user_input in MENU:
        try:
            quantity = int(input("How many cups would you like? "))
            if quantity <= 0:
                print("⚠ Quantity must be greater than zero.")
                continue
        except ValueError:
            print("⚠ Please enter a valid number.")
            continue

        if check_resources(user_input, quantity):
            change = process_payment(MENU[user_input]["cost"], quantity)

            if change is not None:
                make_cofpfee(user_input, quantity)
                print(f"☕ Here is your {user_input} x{quantity}. Enjoy!")
                print(f"💵 Change returned: ${change}\n")

    else:
        print("⚠ Invalid command. Please try again.\n")