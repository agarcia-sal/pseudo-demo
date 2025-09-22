def mc(n, s):
    q, r = divmod(n, s)  # Using divmod to get both quotient and remainder
    if r > 0:
        return r * (q + 1)  # Return modified value if there's a remainder
    else:
        return n  # Return n if no remainder

# Begin Main Block
n, m, s = map(int, input().split())  # Read three integers from user input

# Calculate the result of mc(n, s) and mc(m, s)
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of both results
print(result1 * result2)
