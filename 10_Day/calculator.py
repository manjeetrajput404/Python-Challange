logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def simple_calculator():
    print(logo)
    continue_cal = True

    number1 = int(input("What's the first number?: "))

    while continue_cal:
        print("+  -  *  /")
        operation = input("Pick an operation: ")

        if operation not in ["+", "-", "*", "/"]:
            print("Invalid Operation")
            continue

        number2 = int(input("What's the next number?: "))

        if operation == "+":
            number1 += number2
        elif operation == "-":
            number1 -= number2
        elif operation == "*":
            number1 *= number2
        elif operation == "/":
            number1 /= number2

        con = input(
            f"Type 'y' to continue calculating with {number1}, or type 'n' to start new calculation: "
        )

        if con == 'y':
            continue_cal = True
        elif con == 'n':
            break
        else:
            print("Invalid input")

    return number1   # <-- very important position


result = simple_calculator()
print(result)


    
