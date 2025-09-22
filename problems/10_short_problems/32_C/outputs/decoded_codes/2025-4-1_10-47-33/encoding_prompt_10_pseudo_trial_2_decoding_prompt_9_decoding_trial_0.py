def mc(n, s):
    # Divide n by s to get quotient and remainder
    q, r = divmod(n, s)  # divmod returns both quotient and remainder
    if r > 0:
        return r * (q + 1)  # Return modified value if there is a remainder
    else:
        return n  # Return n if no remainder

# Begin Main Block
n = int(input())  # Read integer n from user input
m = int(input())  # Read integer m from user input
s = int(input())  # Read integer s from user input

# Validate that s is not zero to prevent division errors
if s == 0:
    print("s cannot be zero.")
else:
    # Calculate the result of mc(n, s) and mc(m, s)
    result1 = mc(n, s)
    result2 = mc(m, s)

    # Print the product of both results
    print(result1 * result2)
