def mc(n, s):
    q = n // s          # Calculate quotient using floor division
    r = n % s           # Calculate remainder
    if r > 0:           # Check if remainder exists
        return r * (q + 1)  # Return adjusted value if remainder exists
    else:
        return n        # Return original value if no remainder

# Main program starts here
n = int(input())       # Read integer input for n
m = int(input())       # Read integer input for m
s = int(input())       # Read integer input for s
result1 = mc(n, s)     # Call mc function with n and s
result2 = mc(m, s)     # Call mc function with m and s
print(result1 * result2)  # Output the product of both results
