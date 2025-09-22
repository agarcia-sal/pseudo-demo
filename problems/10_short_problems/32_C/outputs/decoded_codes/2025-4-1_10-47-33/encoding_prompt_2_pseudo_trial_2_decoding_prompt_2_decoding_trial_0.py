def mc(n, s):
    # Calculate quotient and remainder
    quotient = n // s
    remainder = n % s
    
    # Check if remainder is greater than zero
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

# Read a line of input and split it into three integer values
n, m, s = map(int, input().split())

# Calculate the result by multiplying the outputs of mc for n and m with s
result = mc(n, s) * mc(m, s)

# Print the final result
print(result)
