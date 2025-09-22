def calculateRemainderAndAdjustment(number, divisor):
    # Calculate quotient and remainder when dividing number by divisor
    quotient = number // divisor
    remainder = number % divisor
    
    # If there is a remainder
    if remainder > 0:
        # Return the remainder multiplied by incremented quotient
        return remainder * (quotient + 1)
    
    # If no remainder, return the original number
    return number

# Read the input values for n, m, and s and convert them to integers
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
