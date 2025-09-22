def calculate_modified_value(number, divisor):
    # Calculate quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # Check if remainder is greater than zero
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values
value1 = int(input())
value2 = int(input())
divider = int(input())

# Calculate modified values
modified_value1 = calculate_modified_value(value1, divider)
modified_value2 = calculate_modified_value(value2, divider)

# Calculate product
result = modified_value1 * modified_value2

# Display output
print(result)
