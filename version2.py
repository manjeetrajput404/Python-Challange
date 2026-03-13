# Menu provided 
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Resources reserved
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def check_resouces(user_input, quantity):
    res = MENU[user_input]["ingredients"]
    if res["water"]*quantity <= resources["water"] and res["milk"]*quantity <= resources["milk"] and res["coffee"]*quantity <= resources["coffee"]:
        resources["water"] -= res["water"]*quantity
        resources["milk"] -= res["milk"]*quantity
        resources["coffee"] -= res["coffee"]*quantity
        return True
    else:
        print("Insufficient resources")
        return False

def getMoney(cost, quantity):
    global profit
    print("Please, proceed payments...")
    penny = float(input("Enter how many Penny"))
    dime = float(input("Enter how many Dime"))
    nickel = float(input("Enter how many Nickel"))
    quarter = float(input("Enter how many Quarter"))

    user_total_money = (penny * 0.01) + (dime * 0.1) + (nickel * 0.05) + (quarter * 0.25)
    bill = cost * quantity

    if user_total_money >= bill:
        change = user_total_money - bill
        profit += bill
    elif user_total_money < bill:
        print("Insufficient Money")
        exit()
    return change

def report():
    for key, value in resources.items():
        print(f"{key}: {value}")


# print(MENU["latte"].values())
end = True
while end: 
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input in MENU.keys():
        cost = MENU[user_input]["cost"]
        quantity = int(input("Enter how much quantity you wants"))
        availability = check_resouces(user_input, quantity)
        if availability:
            change = getMoney(cost, quantity)
            print(f"Your change is {change}")
            print(f"Enjoy your {user_input}coffee of {quantity} quantity ") 

    elif user_input == "report":
        report()
        
    elif user_input == "off":
        end = False
    elif user_input == "profit":
        print(f"Toal profit: {profit}")
    else: 
        print("Invalid input")
        exit()
      
        

