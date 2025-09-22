def adjusted_value(value, divisor):
    """Calculate the adjusted value based on division and remainder."""
    quotient, remainder = divmod(value, divisor)  # Get quotient and remainder
    if remainder > 0:  # Check if there is a remainder
        return remainder * (quotient + 1)  # Return adjusted value
    else:
        return value  # Return original value if perfectly divisible

# Read input values
n = int(input())  # Input for the first value
m = int(input())  # Input for the second value
s = int(input())  # Input for the divisor

# Calculate adjusted values
first_adjusted_value = adjusted_value(n, s)
second_adjusted_value = adjusted_value(m, s)

# Output the product of the two adjusted values
print(first_adjusted_value * second_adjusted_value)


10
15
5


25
