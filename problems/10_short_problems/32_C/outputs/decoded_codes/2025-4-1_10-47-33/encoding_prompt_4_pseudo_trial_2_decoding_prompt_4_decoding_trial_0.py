def mc(number, size):
    """
    Adjusts the number based on the size. 
    If there is a remainder when dividing, it computes an adjusted value.
    Returns the adjusted value or the original number if there's no remainder.
    """
    quotient, remainder = divmod(number, size)
    if remainder > 0:
        return remainder * (quotient + 1)  # Calculate adjusted value
    else:
        return number  # Return the original number if no remainder

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate and print the product of adjusted values for n and m
result = mc(n, s) * mc(m, s)
print(result)
