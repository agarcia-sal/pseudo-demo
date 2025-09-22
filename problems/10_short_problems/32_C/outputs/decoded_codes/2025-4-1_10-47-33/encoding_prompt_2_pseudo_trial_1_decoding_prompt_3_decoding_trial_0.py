def mc(total_items, group_size):
    """
    This function calculates the total items needed to form complete groups
    and account for any incomplete groups based on the group size.
    """
    complete_groups = total_items // group_size  # Calculate complete groups
    remainder = total_items % group_size   # Find the remainder
    
    if remainder > 0:  # If there are incomplete groups
        additional_items = (complete_groups + 1) * remainder  # Calculate additional items needed
        return additional_items
    else:  # No remainder, return original total
        return total_items

# Read input values
total_items_for_first_case, total_items_for_second_case, group_size = map(int, input().split())

# Calculate results
first_result = mc(total_items_for_first_case, group_size)
second_result = mc(total_items_for_second_case, group_size)

# Output the product of both results
final_result = first_result * second_result
print(final_result)
