# Write a Python program that create a menu-driven program that allows the user to perform various operations (e.g., add, subtract, multiply, divide). Use conditional statements to navigate between options.

print("*******Menu Driven Calculator*******")
x= int(input("Enter 1st Number: "))
y= int(input("Enter 2nd Number: "))

print("\n Enter 1 For Addition")
print(" Enter 2 For substraction")
print(" Enter 3 For multiplication")
print(" Enter 4 For division")

u= int(input("\n Enter a Choice: "))
if u==1:
	print("Addition: ", x+y)
elif u==2:
	print("Substraction: ", x-y)
elif u==3:
	print("Multiplication: ", x*y)
elif u==4:
	print("Division: ", x/y)
else:
	print("Invalid Choice")

print("Thank You for using our calculator")
