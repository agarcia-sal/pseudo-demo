def calculate_groups(total_items, group_size):
    """
    Calculate the number of items in incomplete groups based on total_items and group_size.
    
    Parameters:
    total_items (int): The total number of items.
    group_size (int): The size of each group.
    
    Returns:
    int: The number of items in the last incomplete group or total_items if no incomplete group exists.
    """
    quotient = total_items // group_size
    remainder = total_items % group_size
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_items

# Input Data
total_a = int(input())
total_b = int(input())
group_size = int(input())

# Compute Group Values
value_a = calculate_groups(total_a, group_size)
value_b = calculate_groups(total_b, group_size)

# Calculate and Print Result
result = value_a * value_b
print(result)
