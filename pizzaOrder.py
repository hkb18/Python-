print("Welcome to Python Pizza Deliverires!")
size = input("What size of pizza do u want ? S ,M or L: ")
add_pepperoni = input("Do you want pepperoni ? Y or N: ")
extra_cheese = input("Do you want extra cheese ? Y or N: ")

total_bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25

if size == "L":
    total_bill += large_pizza

elif size == "M":
    total_bill += medium_pizza

elif size == "S":
    total_bill += small_pizza

if add_pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"Total bill is ${total_bill}")
