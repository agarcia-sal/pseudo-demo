def CalculateRemainderSum(dividend, divisor):
    # Divide the dividend by divisor to get the quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # If there is a remainder, return the product of remainder and (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend  # If no remainder, return the original dividend

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate the modified sum for n and m using the CalculateRemainderSum function
resultN = CalculateRemainderSum(n, s)
resultM = CalculateRemainderSum(m, s)

# Output the product of the two results
print(resultN * resultM)
