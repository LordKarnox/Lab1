"""
Program: UPC Validator
Author: Pattharasittha Deevech
Purpose: Validate a 12-digit UPC-A code by calcing the expected numbers and comparing it with the check digit provided.
Starter code: https://stackoverflow.com/questions/67341806/create-check-digit-function
Algorithm reference: https://en.wikipedia.org/wiki/Universal_Product_Code 
Date: 10/6/2026
"""
# Calculate the expected check digit
def find_UPC(first_11_digits):
    odd_sum = 0
    even_sum = 0

    for index in range(11):
        digit = int(first_11_digits[index])
        if index % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    total = odd_sum * 3 + even_sum
    check_digit = (10 - total % 10) % 10
    return check_digit

# Get user input
while True:
    upc = input("Enter a 12-digit UPC: ")

    if len(upc) == 12 and upc.isascii() and upc.isdigit():
        break

    print("Invalid input. Enter exactly 12 digits (0-9).")

first_11_digits = upc[:11]
provided_check_digit = int(upc[11])

# Display the info
print(f"\nThe first 11 digits are '{first_11_digits}'.")
print(f"The provided check digit is '{provided_check_digit}'.")
print("\nCalculating...")

expected_check_digit = find_UPC(first_11_digits)
print(f"The expected check digit is {expected_check_digit}.")

if expected_check_digit == provided_check_digit:
    print("\nThis is a VALID UPC.")
else:
    print("\nThis is an INVALID UPC.")
