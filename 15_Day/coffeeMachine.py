resources = {
    "water": 5000, # ml
    "milk": 2000,  #ml
    "coffee": 1000   #grams
}

def updating_resources(coffee_taste, quantity):
    if coffee_taste == "espresso":
        resources["water"] -= (500 * quantity)
        resources["coffee"] -= (18 * quantity)
    elif coffee_taste == "latte":
        resources["water"] -= (200 * quantity)
        resources["coffee"] -= (28 * quantity)
        resources["milk"] -= (150 * quantity)
    elif coffee_taste == "cappuccino":
        resources["water"] -= (500 * quantity)
        resources["coffee"] -= (18 * quantity)
        resources["milk"] -= (100 * quantity)
    

def report():
    for key , value in resources.items():
        print(f"{key}: {value}")

def making_bill(price):
    quantity = int(input("Enter the quantity of coffee"))
    bill = quantity * price
    return bill, quantity

def proceed_money(bill):
    penny = float(input("Enter how many Penny"))
    dime = float(input("Enter how many Dime"))
    nickel = float(input("Enter how many Nickel"))
    quarter = float(input("Enter how many Quarter"))

    user_total_money = (penny * 0.01) + (dime * 0.1) + (nickel * 0.05) + (quarter * 0.25)

    if user_total_money >= bill:
        change = user_total_money - bill
    elif user_total_money < bill:
        print("Insufficient Money")
        exit()
    return change
    
end = True
while end: 
    
    user_input = input("What do you want? (which coffee)").lower()
    bill = 0

    if user_input == "end":
        end = "Flase"
        exit()
    elif user_input == "report":
        report()


    elif user_input == "espresso":
        price = 1.0
        bill, quantity = making_bill(price)
        updating_resources(user_input , quantity)

    elif user_input == "latte":
        price = 1.5
        bill, quantity = making_bill(price)
        updating_resources(user_input , quantity)

    elif user_input == "cappuccino":
        price = 2.5
        bill, quantity = making_bill(price)
        updating_resources(user_input , quantity)

    else:
        print("Invalid Input")
        exit

    print(f"Your total bill is {bill}, Procedding payment....")
    change = proceed_money(bill)


    print(f"Your change is {change}")



Menu = {
    "espresso": {
    "ingredients": {
        "water": 50,
        "coffee": 18,
    },
    "cost": 1.5
},

    "latte":{
        "water": 200,
        "coffee":28,
        "milk":150,
        "price":1.5
    },
    "cappuccino":{
        "water":500,
        "coffee":18,
        "milk":100,
        "price":2.5
    }
}