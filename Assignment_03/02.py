# Write a Python program by creating a function ‘calculate_area’ that calculates and returns the area of a rectangle. The function should take two parameters: length and width. Test the function with different values.

def calculate_area(length, width):
    area = length * width
    return area

length1 = 5
width1 = 3
area1 = calculate_area(length1, width1)
print("Area of rectangle with length {} and width {}: {}".format(length1, width1, area1))

length2 = 7
width2 = 4
area2 = calculate_area(length2, width2)
print("Area of rectangle with length {} and width {}: {}".format(length2, width2, area2))

length3 = 10
width3 = 6
area3 = calculate_area(length3, width3)
print("Area of rectangle with length {} and width {}: {}".format(length3, width3, area3))
