def calculate_groups(total_items, group_size):
    """
    Calculate the contribution of incomplete groups from total_items.
    
    Args:
    total_items (int): The total number of items.
    group_size (int): The size of each group.

    Returns:
    int: The calculated value based on complete and incomplete groups.
    """
    quotient = total_items // group_size
    remainder = total_items % group_size
    
    if remainder != 0:
        return remainder * (quotient + 1)
    else:
        return total_items

# Input Data
totalA = int(input())
totalB = int(input())
groupSize = int(input())

# Compute Group Values
valueA = calculate_groups(totalA, groupSize)
valueB = calculate_groups(totalB, groupSize)

# Calculate and Print Result
result = valueA * valueB
print(result)
