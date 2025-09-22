def mc(number, size):
    """
    Calculate the adjusted value based on the given parameters.
    
    Parameters:
    number (int): The number to be adjusted.
    size (int): The size to divide the number by.
    
    Returns:
    int: The adjusted value or the original number if no adjustment is needed.
    """
    quotient, remainder = divmod(number, size)  # DIVIDE number BY size
    if remainder > 0:  # Check for remainder
        return remainder * (quotient + 1)  # Calculate adjusted value
    else:
        return number  # Return the original number if no remainder


# Read input values for n, m, and s
n = int(input())  # Read first integer input for n
m = int(input())  # Read second integer input for m
s = int(input())  # Read third integer input for s

# Calculate and print the product of adjusted values for n and m
result = mc(n, s) * mc(m, s)  # Calculate product of adjusted values
print(result)  # Print the result
