def mc(n, s):
    q, r = divmod(n, s)  # Use divmod to get quotient and remainder
    if r > 0:
        return r * (q + 1)  # if there's a remainder, calculate new value
    else:
        return n  # if no remainder, return n

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of two modified values using the mc function
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
