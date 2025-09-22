def calculate_modified_value(number, divisor):
    # Compute the quotient and the remainder when dividing number by divisor
    quotient = number // divisor
    remainder = number % divisor
    
    # Check if the remainder is greater than zero
    if remainder > 0:
        # Return the product of remainder and (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # Return the original number if remainder is zero
        return number

# Read three integers from input
value1 = int(input())
value2 = int(input())
divider = int(input())

# Calculate modified values using the defined function
modified_value1 = calculate_modified_value(value1, divider)
modified_value2 = calculate_modified_value(value2, divider)

# Compute the product of the two modified values
result = modified_value1 * modified_value2

# Print the resulting product
print(result)
