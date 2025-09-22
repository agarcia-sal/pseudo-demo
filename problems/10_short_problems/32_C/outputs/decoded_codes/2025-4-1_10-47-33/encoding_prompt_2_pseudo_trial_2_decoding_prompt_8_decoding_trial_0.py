def mc(n, s):
    quotient = n // s
    remainder = n % s

    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

# Read input and split into three values
n, m, s = map(int, input().split())

# Calculate the result
result = mc(n, s) * mc(m, s)

# Print the final result
print(result)
