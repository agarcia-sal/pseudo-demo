def mc(n, s):
    # Calculate the number of complete groups (q) and the leftover (r)
    q = n // s  # Quotient: number of full groups
    r = n % s   # Remainder: leftover

    # If there is a remainder, return leftover multiplied by (q + 1)
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

# Output the final result
print(result)
