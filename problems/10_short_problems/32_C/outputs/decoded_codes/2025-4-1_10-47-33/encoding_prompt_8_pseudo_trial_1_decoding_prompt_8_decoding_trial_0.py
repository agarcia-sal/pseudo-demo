def calculateRemainderAndAdjustment(number, divisor):
    quotient, remainder = divmod(number, divisor)  # Using divmod to get quotient and remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    return number

# Read input values for n, m, and s and convert them to integers
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted values for n and m using the helper function
adjustedValueForN = calculateRemainderAndAdjustment(n, s)
adjustedValueForM = calculateRemainderAndAdjustment(m, s)

# Compute the final result by multiplying the adjusted values for n and m
finalResult = adjustedValueForN * adjustedValueForM

# Print the final result
print(finalResult)
