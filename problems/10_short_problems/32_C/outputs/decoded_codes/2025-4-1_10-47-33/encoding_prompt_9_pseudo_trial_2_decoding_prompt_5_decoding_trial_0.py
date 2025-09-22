def adjusted_value(value, divisor):
    # Calculate quotient and remainder of the division
    quotient = value // divisor
    remainder = value % divisor

    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

# Read input values n, m, and s from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted values for n and m
first_adjusted_value = adjusted_value(n, s)
second_adjusted_value = adjusted_value(m, s)

# Output the product of the two adjusted values
print(first_adjusted_value * second_adjusted_value)
