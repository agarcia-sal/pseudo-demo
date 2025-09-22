def adjustedValue(value, divisor):
    quotient = value // divisor
    remainder = value % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate adjusted values
firstAdjustedValue = adjustedValue(n, s)
secondAdjustedValue = adjustedValue(m, s)

# Output the product
print(firstAdjustedValue * secondAdjustedValue)
