# Write a Python program that generate and display the multiplication table of a given number using a loop. Allow the user to specify the number.

print("*****Multiplication Table*******")
num= int(input("Enter a Number: "))
for i in range(1,11):
	print(num, "x", i, "=", num*i)
