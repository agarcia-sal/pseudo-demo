def mc(number, size):
    # Divide number by size, storing the quotient and remainder
    q = number // size
    r = number % size
    
    # Adjust the result based on the remainder
    if r > 0:
        return r * (q + 1)  # Calculate adjusted value if remainder exists
    else:
        return number  # Return original number if no remainder

# Read input values from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate result using the 'mc' function for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
