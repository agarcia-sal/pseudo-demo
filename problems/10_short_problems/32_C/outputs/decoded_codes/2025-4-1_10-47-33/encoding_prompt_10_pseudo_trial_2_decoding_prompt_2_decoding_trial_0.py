def mc(n, s):
    q, r = divmod(n, s)  # q is the quotient, r is the remainder
    if r > 0:
        return r * (q + 1)  # When there's a remainder, return the modified value
    else:
        return n  # If no remainder, return n as is

# Begin Main Block
n, m, s = map(int, input().split())  # Read n, m, s from user input

# Calculate the result of mc(n, s) and mc(m, s)
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of both results
print(result1 * result2)
