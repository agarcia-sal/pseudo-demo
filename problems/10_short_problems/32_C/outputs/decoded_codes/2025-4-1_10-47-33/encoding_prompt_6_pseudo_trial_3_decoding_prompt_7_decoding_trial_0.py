def CalculateRemainderAndAdjustCount(dividend, divisor):
    # Calculate the quotient and remainder of the division
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # If there is a remainder, adjust the count by returning remainder multiplied by (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If no remainder, return the original dividend
        return dividend

# Read inputs for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted counts for n and m using the function
adjustedCountForN = CalculateRemainderAndAdjustCount(n, s)
adjustedCountForM = CalculateRemainderAndAdjustCount(m, s)

# Calculate and print the product of adjusted counts for n and m
print(adjustedCountForN * adjustedCountForM)
