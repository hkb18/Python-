# 1 year -> 365 days, 52 weeks ,12 months
age = input("What is your age?")
days = int(365)
months = int(12)
weeks = int(52)
days_in_a_90yr = int(days*90)
months_in_a_90yr = int(months*90)
weeks_in_a_90yr = int(weeks*90)
# print(days_in_a_90yr, months_in_a_90yr, weeks_in_a_90yr)
your_days = int(age)*days
your_weeks = int(age)*weeks
your_months = int(age)*months
# print(your_days, your_months, your_weeks)
print(f"You have {days_in_a_90yr-your_days} days,  {weeks_in_a_90yr-your_weeks} weeks ,{months_in_a_90yr-your_months} months, left")
