def CalculateRemainderSum(dividend, divisor):
    # Divide the dividend by divisor to get the quotient and remainder
    quotient = dividend // divisor  # Integer division to get the quotient
    remainder = dividend % divisor    # Modulus operation to get the remainder
    
    # If there is a remainder, return the product of remainder and (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend  # If no remainder, return the original dividend

# Read input values from standard input
n = int(input())  # First value
m = int(input())  # Second value
s = int(input())  # Third value

# Calculate the modified sum for n and m using the CalculateRemainderSum function
resultN = CalculateRemainderSum(n, s)  # Result for n
resultM = CalculateRemainderSum(m, s)  # Result for m

# Output the product of the two results
print(resultN * resultM)
