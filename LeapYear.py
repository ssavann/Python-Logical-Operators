#calculate if it's a leap year
year = int(input("Which year do you want to check? "))


if year % 4 == 0:				#firt one to check: must be true, to continue the condition

	if year % 100 == 0:			#second one to check: must be false "1" to be Leap year. If not, go to next condition

		if year % 400 == 0:		#third one to check: must be True, False and True to be Leap at this condition
			print(f"So the year {year} is a leap year")
		else:
			print(f"So the year {year} is NOT a leap year")

	else:
		print(f"So the year {year} is a leap year")

else:
	print(f"So the year {year} is NOT a leap year")









