def mc(n, s):
    # Divide n by s to find out how many full groups (q) can be formed
    # and what is the leftover (r)
    q, r = divmod(n, s)  # This function returns the quotient and remainder
    
    # If there is a remainder (r is greater than 0),
    # return the leftover multiplied by (q + 1)
    if r > 0:
        return r * (q + 1)
    else:
        return n  # If no remainder, return n as it is

# Read input values for n, m, and s from standard input
n, m, s = map(int, input().split())

# Calculate the product of the results from mc for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
