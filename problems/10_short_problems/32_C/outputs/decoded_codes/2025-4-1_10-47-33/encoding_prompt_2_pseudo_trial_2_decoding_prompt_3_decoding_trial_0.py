def mc(n, s):
    # Calculate the quotient and remainder of n divided by s
    quotient = n // s
    remainder = n % s
    
    # If the remainder is greater than zero, return the product of remainder and (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If the remainder is zero, return the original number n
        return n

# Read a line of input and split it into three integer values: n, m, and s
n, m, s = map(int, input().split())

# Calculate the result as the product of mc applied to n and m with s
result = mc(n, s) * mc(m, s)

# Print the final result
print(result)
