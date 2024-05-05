# Write a function ‘get_math_function(operation)’ that takes an operation (e.g., "add," "subtract") and returns the corresponding mathematical function. Use this function to perform operations on numbers.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def get_math_function(operation):
    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
    elif operation == "multiply":
        return multiply
    elif operation == "divide":
        return divide
    else:
        return None

operation = "add"
math_func = get_math_function(operation)
if math_func:
    print(operation, "result:", math_func(5, 3))

operation = "subtract"
math_func = get_math_function(operation)
if math_func:
    print(operation, "result:", math_func(5, 3))

operation = "multiply"
math_func = get_math_function(operation)
if math_func:
    print(operation, "result:", math_func(5, 3))

operation = "divide"
math_func = get_math_function(operation)
if math_func:
    print(operation, "result:", math_func(6, 3))
