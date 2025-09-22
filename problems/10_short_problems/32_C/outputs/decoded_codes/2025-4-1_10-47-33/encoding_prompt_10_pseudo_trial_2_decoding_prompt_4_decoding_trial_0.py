def mc(n, s):
    """Calculate modified quotient based on inputs n and s."""
    q, r = divmod(n, s)  # divmod returns both quotient and remainder
    if r > 0:
        return r * (q + 1)  # Adjust value when there's a remainder
    else:
        return n  # Return n when there is no remainder

# Begin Main Block
# Read input from user
n, m, s = map(int, input().split())

# Calculate the result of mc(n, s) and mc(m, s)
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of both results
print(result1 * result2)
