# Write a Python program to generate and display the first N terms of the Fibonacci sequence using a for loop. Allow the user to specify the value of N.

N = int(input("Enter the number of terms (N) for Fibonacci sequence: "))

a, b = 0, 1
fib_sequence = []

for _ in range(N):
    fib_sequence.append(a)
    a, b = b, a + b

print("Fibonacci sequence of", N, "terms:")
print(*fib_sequence)
