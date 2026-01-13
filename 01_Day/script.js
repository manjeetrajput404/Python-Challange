// # Band name generator

// # print("Welcome to Band Name Generator")

// # city_name = input("What's the name of the city you grew up in?\n")
// # pet_name = input("What's your pet's name?\n")

// # print(f"Your band name could be {city_name} {pet_name}")

console.log("Welcome to Band Name Generator")
let city_name = prompt("What's the name of the city you grew up in? \n")
let pet_name = prompt("What's your pet's name? \n")

console.log(`Your band name could be ${city_name} ${pet_name}`)

















// # --------------------------------------
// # Tip Calculator Program
// # --------------------------------------

// print("Welcome to the Tip Calculator!\n")
// total_bill = float(input("What was the total bill? ₹ "))
// tip_percentage = float(input("How much tip would you like to give? (10, 12, or 15): "))
// tip_amount = total_bill * (tip_percentage / 100)
// total_amount = total_bill + tip_amount
// total_people = int(input("How many people to split the bill? "))
// amount_per_person = total_amount / total_people
// amount_per_person = round(amount_per_person, 2)
// print(f"\nEach person should pay: ₹ {amount_per_person}")

console.log("Welcome to the Tip Calculator! \n")
let total_bill = prompt("What was the total bill? ")
let tip_percentage = prompt("How much tipo would you like to give?")
let tip_amount = total_bill * (tip_percentage / 100)
let total_amount = total_bill + tip_amount
let total_people = prompt("How many people to split the bill?")
let amount_per_person = total_amount / total_people
console.log(`Each person should pay: $ ${amount_per_person}`)

