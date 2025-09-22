def mc(number, size):
    """
    Calculate how many complete groups of 'size' can fit into 'number'.
    If there's any remainder, return the remainder multiplied by the next group size.
    """
    quotient, remainder = divmod(number, size)
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read three integers from input: 'n', 'm', and 's'
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of the results of 'mc' for 'n' and 'm', and print the result
result = mc(n, s) * mc(m, s)
print(result)
