# Brian Doheny
# This program will calculate the user's BMI score based of of their height and weight

# Ask user to input their height and weight. Specifically asking for CMs and KGs.
height = float(input("Please enter your height (CMs): "))
weight = float(input("Please enter uour weight (KGs): "))

# Calculating the user's BMI based on their inputs.
bmi = weight / (height/100)**2

# Rounding the BMI figure to 2 decimal places, just to keep it tidy for the user.
bmi = round(bmi,2)


# Adding some flow to the program so that we can tell the user where they sit on the BMI scale based on those inputs.
print("Your BMI score is: ", bmi)
if bmi >= 30:
    print("This is classed as 'Obese' (BMI 30+)")
elif 25 < bmi < 29.9:
    print ("This is classed as 'Overweight' (BMI 25-29.9)")
elif 18.5 < bmi < 24.9:
    print("This is classed as 'Healthy' (BMI 18.5-24.9)")
else:
    print ("This is classed as 'Underweight' (BMI less than 18.5)")