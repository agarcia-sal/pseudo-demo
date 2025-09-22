def mc(n, s):
    # Divide n by s to get quotient and remainder
    q, r = divmod(n, s)
    
    # Check if remainder is greater than zero
    if r > 0:
        # If there is a remainder, calculate and return extended value
        return r * (q + 1)
    else:
        # If there is no remainder, return n
        return n

# Read input values for n, m, and s
n, m, s = map(int, input().split())

# Calculate the product of mc(n, s) and mc(m, s)
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
