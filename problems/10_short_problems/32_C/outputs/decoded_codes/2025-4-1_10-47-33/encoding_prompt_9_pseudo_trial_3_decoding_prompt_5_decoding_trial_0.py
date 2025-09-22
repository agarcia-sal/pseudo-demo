def calculate_modified_value(number, divisor):
    # Calculate the quotient and remainder when dividing the number by the divisor
    quotient = number // divisor
    remainder = number % divisor

    # If the remainder is greater than zero, compute the modified value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If no remainder, return the original number
        return number

# Read input values for value1, value2, and divider
value1 = int(input())
value2 = int(input())
divider = int(input())

# Calculate the modified values for value1 and value2
modified_value1 = calculate_modified_value(value1, divider)
modified_value2 = calculate_modified_value(value2, divider)

# Calculate the product of the two modified values
result = modified_value1 * modified_value2

# Display the resulting product
print(result)
