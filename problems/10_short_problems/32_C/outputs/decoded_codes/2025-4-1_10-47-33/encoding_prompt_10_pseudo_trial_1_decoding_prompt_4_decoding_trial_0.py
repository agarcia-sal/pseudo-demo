def mc(n, s):
    """Calculate adjusted value based on quotient and remainder of n divided by s."""
    q = n // s  # Calculate quotient
    r = n % s   # Calculate remainder

    if r > 0:
        return r * (q + 1)  # Return adjusted value if remainder exists
    else:
        return n  # Return original value if no remainder

# Main program starts here
n = int(input())  # Read integer n from input
m = int(input())  # Read integer m from input
s = int(input())  # Read integer s from input

result1 = mc(n, s)  # Call mc function with n and s
result2 = mc(m, s)  # Call mc function with m and s

print(result1 * result2)  # Output the product of both results
