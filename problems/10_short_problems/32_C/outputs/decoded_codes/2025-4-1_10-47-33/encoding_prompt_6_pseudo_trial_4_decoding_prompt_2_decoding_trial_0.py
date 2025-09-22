def CalculateRemainder(n, s):
    # Divide n by s to get the quotient and remainder
    quotient = n // s
    remainder = n % s
    
    # If there is a remainder, return it multiplied by (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return n
        return n

# Read three integers from input
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted values using the CalculateRemainder function
adjustedValueForN = CalculateRemainder(n, s)
adjustedValueForM = CalculateRemainder(m, s)

# Calculate the final result by multiplying the two adjusted values
finalResult = adjustedValueForN * adjustedValueForM

# Output the final result
print(finalResult)
