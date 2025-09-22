def adjustedValue(value, divisor):
    # Calculate quotient and remainder when value is divided by divisor
    quotient = value // divisor
    remainder = value % divisor
    
    # Check if there's a remainder
    if remainder > 0:
        # If there is a remainder, return the adjusted value
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return the original value
        return value

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate first and second adjusted values using the adjustedValue function
firstAdjustedValue = adjustedValue(n, s)
secondAdjustedValue = adjustedValue(m, s)

# Output the product of the two adjusted values
print(firstAdjustedValue * secondAdjustedValue)
