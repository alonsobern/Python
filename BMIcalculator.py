print("BMI CALCULATOR")

mass = input("Enter your body mass (KG): ")
height = input("Enter your height (Meters): ")
bmi = round((float(mass)/pow(float(height),2)),2)
result = "Your BMI is {}.".format(bmi)

print(result)