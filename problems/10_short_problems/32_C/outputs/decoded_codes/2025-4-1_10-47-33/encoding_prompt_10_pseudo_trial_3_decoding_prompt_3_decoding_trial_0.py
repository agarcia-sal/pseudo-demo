def mc(n, s):
    """
    Calculates a specific value based on the inputs n and s.
    
    If there is a remainder when n is divided by s, the function returns
    the remainder multiplied by one more than the quotient. Otherwise, 
    it returns n.

    Parameters:
    n (int): The first integer input.
    s (int): The second integer input (must be greater than zero).
    
    Returns:
    int: The calculated value based on n and s.
    """
    # Calculate quotient and remainder of n divided by s
    q, r = divmod(n, s)
    
    # Check if remainder is greater than zero
    if r > 0:
        # If there is a remainder, return the computed extended value
        return r * (q + 1)
    else:
        # If there is no remainder, return n
        return n


# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of mc(n, s) and mc(m, s)
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
