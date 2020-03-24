# Brian Doheny
# This program will calculate the user's BMI score based of of their height and weight

# Ask user to input their height and weight. Specifically asking for CMs and KGs here as they are required for this calculation.
weight = float(input("Enter weight (KGs): "))
height = float(input("Enter height (CMs): "))

# Calculating the user's BMI based on their inputs.
# Weight doesn't need any changing as captured in KG already, but the Height needs to be coverted in Metres (rather than the CMs captured).
# Therefore height is divided by 100 first to give the Metres value, which can then be squared.
# The weight is then divided by the height in metres squared.
# Rounding the BMI figure to 2 decimal places, just to keep it tidy for the user. 

bmi = round(weight / (height/100)**2,2)



print("BMI is ", bmi)
# In a real example, I would add some flow to the program so that we can tell the user where they sit on the BMI scale based on those inputs.
# The score on its own doesn't provide all the context the user needs to understand what their BMI means.

# if bmi >= 30:
    # print("This is classed as 'Obese' (BMI 30+)")
# elif 25 < bmi < 29.9:
    # print ("This is classed as 'Overweight' (BMI 25-29.9)")
# elif 18.5 < bmi < 24.9:
    # print("This is classed as 'Healthy' (BMI 18.5-24.9)")
# else:
    # print ("This is classed as 'Underweight' (BMI less than 18.5)")