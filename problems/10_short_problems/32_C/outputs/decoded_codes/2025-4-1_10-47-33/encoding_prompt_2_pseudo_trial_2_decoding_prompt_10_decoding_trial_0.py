def mc(n, s):
    """
    Calculate a modified value based on the division of n by s.
    
    Args:
    n (int): The number to be divided.
    s (int): The divisor.

    Returns:
    int: The result based on the quotient and remainder from the division of n by s.
    """
    quotient = n // s
    remainder = n % s
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n


# Read input from the user
input_values = input().split()
n = int(input_values[0])
m = int(input_values[1])
s = int(input_values[2])

# Calculate the result using the mc function
result = mc(n, s) * mc(m, s)

# Print the final result
print(result)
