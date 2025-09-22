def mc(n, s):
    # Calculate quotient and remainder when dividing n by s
    q, r = divmod(n, s)
    
    # If there's a remainder, return the leftover multiplied by (q + 1)
    if r > 0:
        return r * (q + 1)
    else:
        return n  # If no remainder, return n as it is

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of mc results for n and m with the same s
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
