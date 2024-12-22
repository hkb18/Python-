import random
no_of_letters = int(
    input("How many LETTERS would you like in your password?\n"))
no_of_symbols = int(
    input("How many SYMBOLS would you like in your password?\n"))
no_of_numbers = int(
    input("How many NUMBER would you like in your password?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '_']

print("WELCOME TO  RANDOM PASSWORD GENERATOR!🤫")
password_list = []

for char in range(0, no_of_letters):
    password_list.append(random.choice(letters))
for digit in range(0, no_of_numbers):
    password_list += random.choice(numbers)
for sym in range(0, no_of_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")
