def calculate_modified_value(number, divisor):
    # Calculate the quotient and the remainder of the number divided by the divisor
    quotient = number // divisor
    remainder = number % divisor
    
    # If the remainder is greater than zero, calculate the modified value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If not, return the original number
        return number

# Read input values
value1 = int(input())
value2 = int(input())
divider = int(input())

# Calculate modified values using the defined function
modified_value1 = calculate_modified_value(value1, divider)
modified_value2 = calculate_modified_value(value2, divider)

# Calculate the product of the modified values
result = modified_value1 * modified_value2

# Display the resulting product
print(result)
