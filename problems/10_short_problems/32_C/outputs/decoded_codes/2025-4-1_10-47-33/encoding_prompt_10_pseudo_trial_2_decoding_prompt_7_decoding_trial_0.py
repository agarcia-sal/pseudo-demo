def mc(n, s):
    # Calculate the quotient and remainder of n divided by s 
    q, r = divmod(n, s)  # divmod returns both quotient and remainder
    # Check if there is a remainder
    if r > 0:
        return r * (q + 1)  # When there's a remainder, return the modified value
    else:
        return n  # If no remainder, return n as is

# Begin Main Block
# Read three integers from user input
n = int(input())  # Input for n
m = int(input())  # Input for m
s = int(input())  # Input for s

# Ensure s is not zero to prevent division errors
if s == 0:
    raise ValueError("s cannot be zero.")

# Calculate the result of mc(n, s) and mc(m, s)
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of both results
print(result1 * result2)
