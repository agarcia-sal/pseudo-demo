def CalculateMaxCount(n, s):
    q = n // s           # Integer division to get quotient
    r = n % s            # Modulus operation to get remainder
    if r > 0:
        return r * (q + 1)  # Multiply remainder by (quotient + 1)
    else:
        return n          # Return n if remainder is not greater than 0

# Read integers n, m, and s from input
n = int(input())
m = int(input())
s = int(input())

# Calculate count1 and count2
count1 = CalculateMaxCount(n, s)
count2 = CalculateMaxCount(m, s)

# Print the product of count1 and count2
print(count1 * count2)
