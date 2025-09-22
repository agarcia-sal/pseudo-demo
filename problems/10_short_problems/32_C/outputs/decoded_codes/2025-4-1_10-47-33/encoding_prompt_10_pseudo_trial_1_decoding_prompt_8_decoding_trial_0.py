def mc(n, s):
    q = n // s        # Calculate quotient
    r = n % s         # Calculate remainder
    if r > 0:
        return r * (q + 1)  # If remainder exists, return adjusted value
    else:
        return n            # If no remainder, return original value


# Main program starts here
n = int(input())  # Read first integer from input
m = int(input())  # Read second integer from input
s = int(input())  # Read third integer from input

result1 = mc(n, s)  # Call mc function with n and s
result2 = mc(m, s)  # Call mc function with m and s
print(result1 * result2)  # Output the product of both results
