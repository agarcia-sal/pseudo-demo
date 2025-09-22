def mc(n, s):
    # Calculate quotient and remainder
    q = n // s  # Integer division to get the quotient
    r = n % s   # Remainder of n divided by s
    
    # If there is a remainder, return adjusted value
    if r > 0:
        return r * (q + 1)
    else:
        return n  # If no remainder, return the original value

# Main program starts here
# Read three integer values from standard input
n = int(input())
m = int(input())
s = int(input())

# Call mc function with n and s, and with m and s
result1 = mc(n, s)
result2 = mc(m, s)

# Output the product of both results
print(result1 * result2)
