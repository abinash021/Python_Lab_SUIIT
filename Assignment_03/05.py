#  Write a Python program that demonstrates the difference between global and local variables inside and outside a function.


global_var = 10

def my_function():
    local_var = 20
    print("Inside the function:")
    print("Local variable:", local_var) 
    print("Global variable:", global_var)

print("Outside the function:")
print("Global variable:", global_var)

my_function()

