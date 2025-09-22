def mc(n, s):
    q = n // s               # Calculate how many full groups of size s can fit in n
    r = n % s                # Calculate the remainder when n is divided by s
    if r > 0:                # Check if there is a remainder
        return r * (q + 1)   # If there is a remainder, return r multiplied by (q + 1)
    else:
        return n            # If there is no remainder, return n

# Main Execution
n = int(input())           # Read three integers from input
m = int(input())
s = int(input())
result1 = mc(n, s)        # Call mc function with n and s
result2 = mc(m, s)        # Call mc function with m and s
print(result1 * result2)   # Print the product of the two results
