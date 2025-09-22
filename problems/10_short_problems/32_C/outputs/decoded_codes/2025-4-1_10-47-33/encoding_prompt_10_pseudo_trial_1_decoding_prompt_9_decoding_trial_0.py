def mc(n, s):
    # Calculate quotient and remainder
    q = n // s  # Use integer division to get the quotient
    r = n % s   # Get the remainder

    if r > 0:
        return r * (q + 1)  # If there is a remainder, return adjusted value
    else:
        return n  # If no remainder, return the original value

# Main program starts here
n = int(input())  # Read integer n from input
m = int(input())  # Read integer m from input
s = int(input())  # Read integer s from input

result1 = mc(n, s)  # Call mc function with n and s
result2 = mc(m, s)  # Call mc function with m and s

print(result1 * result2)  # Output the product of both results
