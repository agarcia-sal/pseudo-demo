# Define the function mc, which computes a specific value based on n and s
def mc(n, s):
    # Calculate quotient (q) and remainder (r)
    q = n // s  # Integer division to get the number of full groups
    r = n % s   # Modulus to get the leftover

    # Check if there is a remainder
    if r > 0:
        return r * (q + 1)  # If there's leftover, multiply it by (q + 1)
    else:
        return n  # If no remainder, return n as it is

# Read input values for n, m, and s
n = int(input())  # Read integer input for n
m = int(input())  # Read integer input for m
s = int(input())  # Read integer input for s

# Calculate the product of the results from mc for both n and m
result = mc(n, s) * mc(m, s)  # Call mc for both n and m, and calculate their product

# Output the result
print(result)  # Print the final result
