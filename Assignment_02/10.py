'''
Given an input file which contains a list of names and phone numbers separated by spaces in the following format: 
a)	Phone Number contains a 3- or 2-digit area code and a hyphen followed by an 8-digit number.
b)	Find all names having phone numbers with a 3-digit area code using regular expressions.

'''


import re

def find_names_with_three_digit_area_code(file_name):
    pattern = r'(\b[A-Za-z]+\b)\s+\b\d{3}-\d{8}\b'

    names_with_three_digit_area_code = []

    with open(file_name, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
            for match in matches:
                names_with_three_digit_area_code.append(match)

    return names_with_three_digit_area_code

file_name = "phone_numbers.txt" 
names = find_names_with_three_digit_area_code(file_name)
print("Names with phone numbers having a 3-digit area code:")
for name in names:
    print(name)


'''
For example, if your phone_numbers.txt file looks like this:

John 123-456789
Alice 456-123456
Bob 789-987654
Charlie 321-987654
David 654-123456

The output will be:

Names with phone numbers having a 3-digit area code:
Charlie


'''