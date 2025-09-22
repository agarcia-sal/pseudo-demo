def mc(n, s):
    # Calculate the quotient and remainder when n is divided by s
    quotient = n // s
    remainder = n % s
    
    # Check if the remainder is greater than zero
    if remainder > 0:
        # Return the product of the remainder and the sum of the quotient plus one
        return remainder * (quotient + 1)
    else:
        # Return the original number n if remainder is zero
        return n

# Read a line of input and split it into three values, converting them to integers
n, m, s = map(int, input().split())

# Calculate the result by multiplying the output of mc
result = mc(n, s) * mc(m, s)

# Print the final result
print(result)
