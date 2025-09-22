def calculate_modified_value(number, divisor):
    # Compute the quotient and the remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # Check if the remainder is greater than 0
    if remainder > 0:
        # Return the product of the remainder and (the quotient plus one)
        return remainder * (quotient + 1)
    else:
        # Return the original number
        return number

# Read input for three integers
value1 = int(input())
value2 = int(input())
divider = int(input())

# Calculate modified values using the defined function
modified_value1 = calculate_modified_value(value1, divider)
modified_value2 = calculate_modified_value(value2, divider)

# Calculate the product of the two modified values
result = modified_value1 * modified_value2

# Display the resulting product
print(result)
