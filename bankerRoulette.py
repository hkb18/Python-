import random

names_string = input("Give me everbody's names, separated by a comma.")
names = names_string.split(",")

nameslen = len(names)
random_choice = random.randint(0, nameslen - 1)

print(f"{names[random_choice]} is going to buy the meal today")

# EASIER WAY BELOW👇
# person_who_will_pay = random.choice(names)
# print(f"{person_who_will_pay} is going to buy the meals today!")
