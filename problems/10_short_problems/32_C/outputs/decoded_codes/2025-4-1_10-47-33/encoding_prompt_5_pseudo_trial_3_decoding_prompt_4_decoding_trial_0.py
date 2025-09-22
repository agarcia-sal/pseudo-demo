def calculate_groups(total_items, group_size):
    """
    Calculate the number of groups that can be formed from total_items 
    when each group contains group_size items. If there are leftover items,
    an additional group is counted.
    
    Args:
        total_items (int): Total number of items to form groups from.
        group_size (int): Number of items in each group.

    Returns:
        int: Total number of groups that can be formed.
    """
    # Calculate number of full groups and remainder
    number_of_groups = total_items // group_size
    remainder = total_items % group_size

    # If there is a remainder, one more group is needed for the leftovers
    if remainder > 0:
        return number_of_groups + 1
    else:
        return number_of_groups


# Read the three integers from user input
total_items_a = int(input())
total_items_b = int(input())
group_size = int(input())

# Calculate the number of groups for each quantity
groups_a = calculate_groups(total_items_a, group_size)
groups_b = calculate_groups(total_items_b, group_size)

# Calculate the product of groups formed from both quantities
result = groups_a * groups_b

# Print the final result
print(result)
