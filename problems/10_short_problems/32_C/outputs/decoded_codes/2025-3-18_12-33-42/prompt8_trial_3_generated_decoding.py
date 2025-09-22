def calculateAdjustedValue(number, divisor):
    quotient, remainder = divmod(number, divisor)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read three integers from input
n = int(input())
m = int(input())
s = int(input())

# Calculate adjusted values for n and m based on the divisor s
adjustedValueForN = calculateAdjustedValue(n, s)
adjustedValueForM = calculateAdjustedValue(m, s)

# Calculate and print the final product of the two adjusted values
print(adjustedValueForN * adjustedValueForM)
