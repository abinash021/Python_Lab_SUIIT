# Write a Python program that calculates the sum of a series of integers entered by the user. The user should be able to input numbers until they enter a specific sentinel value (e.g., 0), and then display the sum.

sum_of_integers = 0


while True:
    user_input = input("Enter an integer (enter 0 to finish): ")
    if user_input == '0':
        break
    try:
        sum_of_integers += int(user_input)
    except ValueError:
        print("Please enter a valid integer.")

print("The sum of the integers is:", sum_of_integers)
