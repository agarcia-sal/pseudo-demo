def calculate_adjusted_groups(value, group_size):
    """
    Calculate the adjusted value based on how the value divides into groups.
    
    Args:
    value (int): The number to be divided into groups.
    group_size (int): The size of each group.
    
    Returns:
    int: The adjusted value after considering group distribution and any remainders.
    """
    quotient = value // group_size
    remainder = value % group_size
    
    if remainder > 0:
        return remainder * (quotient + 1)  # Include one extra group for the remainder
    else:
        return value  # If there's no remainder, return the original value


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
