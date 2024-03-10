# Write a Python program that checks if a given integer is prime or not. 

number = int(input("Enter a number: "))

if number <= 1:
    print(number, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    print(number, "is a prime number" if is_prime else "is not a prime number")
