# Function to calculate the modified value based on number and size
def mc(number, size):
    # Divide the number by size and get quotient and remainder
    q, r = divmod(number, size)
    # Check if there is a remainder and adjust the value accordingly
    if r > 0:
        return r * (q + 1)  # Adjusted value if remainder exists
    else:
        return number  # Return the original number otherwise

# Read input values n, m, s from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate result using the 'mc' function for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
