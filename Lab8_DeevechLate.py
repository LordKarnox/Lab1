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


