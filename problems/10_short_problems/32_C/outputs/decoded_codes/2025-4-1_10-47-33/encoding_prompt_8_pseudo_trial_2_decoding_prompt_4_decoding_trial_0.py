def calculate_groups(total_quantity, group_size):
    """
    Calculate the effective number of groups based on total quantity and group size.
    
    Args:
        total_quantity (int): The total number of items.
        group_size (int): The size of each group.
        
    Returns:
        int: The effective number of groups calculated based on full groups and remainder.
    """
    full_groups = total_quantity // group_size  # Determine how many full groups can be formed
    remainder = total_quantity % group_size      # Find the count of extra items

    if remainder > 0:  # If there are extra items
        return remainder * (full_groups + 1)     # Return effective groups considering extra items
    else:
        return total_quantity                      # Return total quantity if no extra items

# Main program logic
quantity1 = int(input())  # Read quantity1 from input
quantity2 = int(input())  # Read quantity2 from input
group_size = int(input())  # Read groupSize from input

# Calculate effective groups for both quantities
effective_groups1 = calculate_groups(quantity1, group_size)
effective_groups2 = calculate_groups(quantity2, group_size)

# Multiply the two effective group values to get the final result
final_result = effective_groups1 * effective_groups2

# Output the final result
print(final_result)
