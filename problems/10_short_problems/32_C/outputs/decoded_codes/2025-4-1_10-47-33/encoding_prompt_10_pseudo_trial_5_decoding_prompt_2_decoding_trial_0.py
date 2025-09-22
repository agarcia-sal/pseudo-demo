def CalculateRemainder(n, s):
    # Calculate how many full groups of size s can be made from n
    quotient = n // s
    # Calculate the remainder when n is divided by s
    remainder = n % s
    
    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

# Read input values for n, m, and s from user
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the defined function for n and m
result1 = CalculateRemainder(n, s)
result2 = CalculateRemainder(m, s)

# Print the product of the two results
print(result1 * result2)
