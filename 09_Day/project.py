logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)



persons_dict = {}
decision = "yes"
winner = ""

while not decision == "yes":
    name = input("Enter your name:")
    amount = int(input("Enter the bit amount"))
    persons_dict[name] = {amount}
    
    decision = input("is there is any other person type Yes or No").lower()
    if decision == "yes":
        print("\n\n\n\n\n")
    else:
        for name in persons_dict:
            for others in persons_dict:
                if persons_dict[name] > persons_dict[others]:
                    winner = persons_dict[name]
                

print(f"The winner is {persons_dict} and the amount is {persons_dict[name][amount]} ")

