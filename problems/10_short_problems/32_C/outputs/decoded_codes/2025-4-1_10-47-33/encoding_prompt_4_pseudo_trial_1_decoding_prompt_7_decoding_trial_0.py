def calculateResult(n, m, s):
    # Compute the adjusted value for n based on s
    adjusted_n = computeAdjustedValue(n, s)

    # Compute the adjusted value for m based on s
    adjusted_m = computeAdjustedValue(m, s)
    
    # Calculate the final result by multiplying the adjusted values
    return adjusted_n * adjusted_m

def computeAdjustedValue(value, segmentSize):
    # Divide value into segments and get the quotient and remainder
    quotient, remainder = divmod(value, segmentSize)

    # If there is a remainder, adjust the value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

# Input: Read three integers from standard input (n, m, and s)
n = int(input())  # Read the first integer
m = int(input())  # Read the second integer
s = int(input())  # Read the segment size

# Output: Print the result of the calculation
print(calculateResult(n, m, s))
