height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# bmi=weight/height**2
bmi = round(weight/height**2, 2)
if bmi < 18.5:
    print(f"BMI is {bmi} & its under 18.5 they are underweight")
elif bmi < 25:
    print(f"BMI is {bmi} & its over 18.5 and under 25 they have a normalweight")
elif bmi < 30:
    print(f"BMI is {bmi} & its over 25 and under 30 they are overweight")
elif bmi < 35:
    print(f"BMI is {bmi} & its over 30 and under 35 they are obese")
else:
    print(f"BMI is {bmi} & its over 35 they are clinically obese")
