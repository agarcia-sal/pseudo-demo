def mc(n, s):
    # Calculate the quotient and remainder when n is divided by s
    quotient = n // s
    remainder = n % s
    
    # If the remainder is greater than zero
    if remainder > 0:
        # Return the product of the remainder and the sum of the quotient plus one
        return remainder * (quotient + 1)
    else:
        # If no remainder, return the original number n
        return n

# Read a line of input and split it into three integer values: n, m, and s
n, m, s = map(int, input().split())

# Calculate the result by multiplying the outputs of mc for n and m with s
result = mc(n, s) * mc(m, s)

# Print the final result
print(result)
