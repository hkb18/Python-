bill = float(input("What was the total bill? "))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill with "))

# IF THE BILL WAS $150.00, SPLIT WITH 5 PEOPLE, WITH 12% TIP
#  150 + (12/100) is tip
# total_bill=tip + bill
# EACH PERSON SHOULD PAY (150.00/5)*1.12
# ROUND RESULT TO 2 DECIMAL PLACES

tip = float(bill*(tip_percentage/100))
total_bill = tip+bill
split = total_bill/total_people
message = f"Each person should pay ${round(split,2)}"
print(message)
# tip = float(total_bill+(total_bill*(tip_percentage/100)))
# split = tip/total_people
# print(split)
