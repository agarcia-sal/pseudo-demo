# Define function to calculate modified value based on the algorithm
def calculate_modified_value(number, divisor):
    # Calculate quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # If the remainder is greater than zero, calculate modified value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number  # Return original number if no remainder

# Read input values
value1 = int(input())
value2 = int(input())
divider = int(input())

# Calculate modified values using the defined function
modified_value1 = calculate_modified_value(value1, divider)
modified_value2 = calculate_modified_value(value2, divider)

# Calculate the product of the two modified values
result = modified_value1 * modified_value2

# Print the resulting product
print(result)
