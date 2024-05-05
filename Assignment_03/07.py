# Write a Python program to create a Python decorator called timer that calculates and prints the execution time of a function. Apply this decorator to a sample function.
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timer
def sample_function():
    time.sleep(2)
    print("This is a sample function")

sample_function()
