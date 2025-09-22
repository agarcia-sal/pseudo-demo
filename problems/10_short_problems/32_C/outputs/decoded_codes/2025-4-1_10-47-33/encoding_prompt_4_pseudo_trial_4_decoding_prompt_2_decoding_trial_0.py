def mc(number, size):
    q = number // size  # Integer division for quotient
    r = number % size   # Modulus operator for remainder

    if r > 0:
        return r * (q + 1)  # Adjusted value if remainder exists
    else:
        return number        # Return original number otherwise

# Read input values
n, m, s = map(int, input().split())

# Calculate result using the 'mc' function for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
