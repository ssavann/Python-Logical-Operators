#Love calculator: to find out if you are compatible with the other person
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

totalName1 = 0

combinedString = name1 + name2
lowerCaseString = combinedString.lower()


t = lowerCaseString.count("t")
r = lowerCaseString.count("r")
u = lowerCaseString.count("u")
e = lowerCaseString.count("e")

true = t + r + u + e

l = lowerCaseString.count("l")
o = lowerCaseString.count("o")
v = lowerCaseString.count("v")
e = lowerCaseString.count("e")

love = l + o + v + e

#need to convert "string" into "integer" to be able to compare: love_score < 10
love_score = int(str(true) + str(love))     

if(love_score < 10) or (love_score > 90):
    print(f"your love score is: {love_score}, you to together like coke and mentos.")

elif (love_score >= 40) and (love_score <=50):
    print(f"your love score is: {love_score}, you are alright together.")

else:
    print(f"your love score is: {love_score}")

#try: Kanye West and Kim Kardashian



