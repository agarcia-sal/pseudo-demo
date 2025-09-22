def mc(total_items, group_size):
    """
    Calculate the effective item count based on the total items and group size.
    
    Args:
        total_items (int): Total number of items.
        group_size (int): Size of each group.
    
    Returns:
        int: Effective item count based on groups.
    """
    # Calculate how many full groups can fit and the remainder
    full_groups, remainder = divmod(total_items, group_size)
    
    # Determine the effective item count based on remainder
    if remainder > 0:
        return remainder * (full_groups + 1)  # Count remainder items with an additional group
    else:
        return total_items  # No remainder, return total item count

# Read input values for total items n, additional total m, and group size s
total_items_n = int(input())
additional_total_m = int(input())
group_size_s = int(input())

# Calculate and print the product of the processed item counts for n and m
print(mc(total_items_n, group_size_s) * mc(additional_total_m, group_size_s))
