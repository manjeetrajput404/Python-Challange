import random

# -------------------------------
# DATA SOURCE
# -------------------------------

numbers = ['0','1','2','3','4','5','6','7','8','9']

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
           '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '?', '/']

# -------------------------------
# USER INPUT
# -------------------------------

print("Welcome to the PyPassword Generator! 🔐")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# -------------------------------
# PASSWORD GENERATION
# -------------------------------

password_list = []  # Will store all characters of password

# Add random numbers
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))
    # Alternative:
    # password_list += random.choice(numbers)

# Add random letters
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# -------------------------------
# SHUFFLE TO MAKE PASSWORD STRONG
# -------------------------------

random.shuffle(password_list)
# Alternative method:
# password_list = random.sample(password_list, len(password_list))

# -------------------------------
# CONVERT LIST TO STRING
# -------------------------------

strong_password = ""

for char in password_list:
    strong_password += char

# Alternative:
# strong_password = "".join(password_list)

# -------------------------------
# OUTPUT
# -------------------------------

print("\nYour Strong Password is:")
print(strong_password)
