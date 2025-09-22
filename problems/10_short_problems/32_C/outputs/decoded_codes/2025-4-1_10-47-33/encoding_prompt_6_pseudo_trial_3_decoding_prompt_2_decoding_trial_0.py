def CalculateRemainderAndAdjustCount(dividend, divisor):
    # Calculate how many times the divisor fits into the dividend and the remainder.
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # If there is a remainder, adjust the count
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend  # If no remainder, return the original dividend

# Read inputs for the first value (n), second value (m), and divisor value (s)
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted counts for n and m using the function
adjustedCountForN = CalculateRemainderAndAdjustCount(n, s)
adjustedCountForM = CalculateRemainderAndAdjustCount(m, s)

# Calculate and print the product of adjusted counts for n and m
print(adjustedCountForN * adjustedCountForM)
