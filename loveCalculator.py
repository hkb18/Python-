name1 = input("What is your name: ")
name2 = input("Whats their name: ")

name = name1 + name2
lowercasename = name.lower()

t = lowercasename.count("t")
r = lowercasename.count("r")
u = lowercasename.count("u")
e = lowercasename.count("e")
true = t + r + u + e

l = lowercasename.count("l")
o = lowercasename.count("o")
v = lowercasename.count("v")
e = lowercasename.count("e")
love = l + o + v + e

truelove = int(str(true) + str(love))

if truelove < 10 and truelove > 90:
    print(f"Your score is {truelove} , you are like cola and mentos")
elif truelove > 40 and truelove < 50:
    print(f"Your score is {truelove} , you are fine")
else:
    print(f"Your score is {truelove}")
