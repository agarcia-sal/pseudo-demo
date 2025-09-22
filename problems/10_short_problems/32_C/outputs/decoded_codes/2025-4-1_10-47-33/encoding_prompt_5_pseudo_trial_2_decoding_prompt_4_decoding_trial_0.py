def calculate_adjusted_groups(value, group_size):
    """
    Divides the value into groups of the specified size and adjusts 
    the result based on the remainder.
    
    Args:
    value (int): The number to be divided into groups.
    group_size (int): The size of each group.
    
    Returns:
    int: Adjusted groups product based on the division result.
    """
    quotient, remainder = divmod(value, group_size)  # Efficient way to get quotient and remainder
    
    if remainder > 0:
        return remainder * (quotient + 1)  # Include an extra group if there's a remainder
    else:
        return value  # Return the original value if division is perfect


# Read input values for n, m, and s from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted group values for n and m
adjusted_n = calculate_adjusted_groups(n, s)
adjusted_m = calculate_adjusted_groups(m, s)

# Calculate the product of the two adjusted values
product = adjusted_n * adjusted_m

# Output the result of the product
print(product)
