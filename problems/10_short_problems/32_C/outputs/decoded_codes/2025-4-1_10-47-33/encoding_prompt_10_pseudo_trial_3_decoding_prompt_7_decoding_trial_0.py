def mc(n, s):
    # Calculate quotient and remainder of n divided by s
    q, r = divmod(n, s)
    
    # Check if there is a remainder
    if r > 0:
        # If there is a remainder, calculate and return the extended value
        return r * (q + 1)
    else:
        # If there is no remainder, return n
        return n

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of mc(n, s) and mc(m, s)
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
