def calculate_groups(total_items, group_size):
    """
    Calculate the number of full groups that can be formed from total_items
    using the given group_size, accounting for any remaining items.

    Parameters:
    total_items (int): The total number of items to divide into groups.
    group_size (int): The size of each group.

    Returns:
    int: The number of groups that can be formed.
    """
    number_of_groups, remainder = divmod(total_items, group_size)

    # If there is a remainder, include an extra group for leftover items
    if remainder > 0:
        return number_of_groups + 1
    else:
        return number_of_groups

# Read three integers from user input
total_items_a = int(input())
total_items_b = int(input())
group_size = int(input())

# Calculate the number of groups for each quantity
groups_a = calculate_groups(total_items_a, group_size)
groups_b = calculate_groups(total_items_b, group_size)

# Calculate the product of groups formed from both quantities
result = groups_a * groups_b

# Output the final result
print(result)
