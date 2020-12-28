#Body Mass Index calculation
height = float(input("enter your height in m: "))   #1.80, 1.60
weight = float(input("enter your weight in kg: "))  #60, 80, 100

bmi = round(weight / (height**2))       #need to convert "height" and "weight" into a float


if bmi < 18.5:      #if condition is "False" go to next condition
    print(f"Your BMI is: {bmi} and you are underweight.")

elif bmi < 25:      #if condition is "False" go to next condition
    print(f"Your BMI is: {bmi} and you have normal weight.")

elif bmi < 30:      #if condition is "False" go to next condition
    print(f"Your BMI is: {bmi} and you are overweight.")

elif bmi < 35:      #if condition is "True" output the message
    print(f"Your BMI is: {bmi} and you are obese.")

else:
    print(f"Your BMI is: {bmi} and you are clinically obese.")


