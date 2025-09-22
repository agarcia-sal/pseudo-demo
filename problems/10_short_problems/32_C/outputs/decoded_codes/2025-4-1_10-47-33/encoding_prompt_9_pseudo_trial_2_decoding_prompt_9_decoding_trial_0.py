def adjustedValue(value, divisor):
    # Divide value by divisor and store the quotient and remainder
    quotient = value // divisor
    remainder = value % divisor
    
    # Check if there is a remainder
    if remainder > 0:
        # Return remainder multiplied by (quotient plus one)
        return remainder * (quotient + 1)
    else:
        # If no remainder, return the original value
        return value

# Read input values n, m, s from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate first adjusted value as the result of adjustedValue(n, s)
first_adjusted_value = adjustedValue(n, s)

# Calculate second adjusted value as the result of adjustedValue(m, s)
second_adjusted_value = adjustedValue(m, s)

# Output the product of first_adjusted_value and second_adjusted_value
print(first_adjusted_value * second_adjusted_value)
