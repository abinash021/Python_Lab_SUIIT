age= int(input("Enter Your Age(Between 1-100)"))

if age<=10:
	print("You are a child!")
elif age>=11 and age<=17:
	print("You are a teenager!")
elif age>=18 and age<=35:
	print("You are an Adult!")
elif age>=19 and age<=100:
	print("You are a Senior Citizen!")
else:
	print("Invalid age(Enter a Valid age Between 1-100!)")
