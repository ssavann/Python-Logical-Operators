#Check if my number is Odd or Even. Even number can divide by 2

number = int(input("Which number do you want to check? "))

remainder = number % 2       #10 / 2 = 5, but no remainder

if remainder == 0:
    print(f"{number} is an Even number")

else:
    print(f"{number} is an Odd number")