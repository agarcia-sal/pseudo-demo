def mc(n, s):
    # Calculate how many complete groups of size 's' can be formed and any leftover
    q, r = divmod(n, s)  # divmod returns quotient (q) and remainder (r)
    
    # If there is a remainder, return the leftover multiplied by (q + 1)
    if r > 0:
        return r * (q + 1)
    else:
        return n  # If no remainder, return n as it is

# Read input values for n, m, and s from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of the results from mc for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
