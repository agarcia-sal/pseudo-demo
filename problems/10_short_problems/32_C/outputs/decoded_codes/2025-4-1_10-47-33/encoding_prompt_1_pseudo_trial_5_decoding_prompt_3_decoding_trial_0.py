def mc(n, s):
    # Calculate the quotient and remainder of n divided by s
    q, r = divmod(n, s)  # divmod returns a tuple (quotient, remainder)

    # If there is a remainder, calculate the modified value
    if r > 0:
        return r * (q + 1)
    else:
        return n  # If no remainder, return n as is

# Read input values for n, m, and s from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of the results from mc for both n and m
result = mc(n, s) * mc(m, s)

# Output the final result
print(result)
