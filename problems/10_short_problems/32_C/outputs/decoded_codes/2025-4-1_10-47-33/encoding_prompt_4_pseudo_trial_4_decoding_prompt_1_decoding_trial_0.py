def mc(number, size):
    q, r = divmod(number, size)  # Calculate quotient and remainder
    if r > 0:
        return r * (q + 1)  # Calculate adjusted value if remainder exists
    else:
        return number  # Return original number otherwise

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate result using the 'mc' function for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
