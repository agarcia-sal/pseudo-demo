def adjusted_value(value, divisor):
    """
    Calculate the adjusted value based on the given value and divisor.
    If the value is not perfectly divisible by the divisor,
    return the remainder multiplied by (quotient plus one).
    Otherwise, return the original value.
    """
    quotient, remainder = divmod(value, divisor)  # Calculate quotient and remainder
    if remainder > 0:  # Check if there is any remainder
        return remainder * (quotient + 1)  # Adjust value if remainder exists
    else:
        return value  # Return original value if divisible

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted values
first_adjusted_value = adjusted_value(n, s)
second_adjusted_value = adjusted_value(m, s)

# Output the product of the two adjusted values
product = first_adjusted_value * second_adjusted_value
print(product)
