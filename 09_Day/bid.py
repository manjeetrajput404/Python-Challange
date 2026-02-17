import logo

print(logo.logo)

parties_dict = {}
add_user = "yes"

while add_user == "yes":
    name = input("Enter your name")
    amount = int(input("Enter you bid price"))
    parties_dict[name] = amount

    add_user = (input("If any other user, type Yes or No")).lower()
    if add_user == "yes":
        print("\n\n\n\n\n")
    
winner = ""
max_amount = 0
for user in parties_dict:
    if parties_dict[user] > max_amount:
        winner = user
        max_amount = parties_dict[user]

print(f"Winner is {winner} and the amount is {max_amount}")