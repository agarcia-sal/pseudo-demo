def mc(n, s):
    # Calculate how many full groups of size s can fit in n
    q = n // s  # Integer division
    # Calculate the remainder when n is divided by s
    r = n % s
    # Check if there is a remainder
    if r > 0:
        # If there is a remainder, return r multiplied by (q + 1)
        return r * (q + 1)
    else:
        # If there is no remainder, return n
        return n

# Main Execution
# Read three integers from input
n = int(input())
m = int(input())
s = int(input())

# Call mc function with n and s
result1 = mc(n, s)
# Call mc function with m and s
result2 = mc(m, s)

# Print the product of the two results
print(result1 * result2)
