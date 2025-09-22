def calculate_remainder_multiplier(total_items, group_size):
    """
    Calculate the product of remaining items and one more than the number of full groups,
    or return total_items if there are no remaining items.
    
    Parameters:
        total_items (int): The total number of items.
        group_size (int): The size of each group.
        
    Returns:
        int: The calculated remainder multiplier.
    """
    full_groups = total_items // group_size
    remaining_items = total_items % group_size

    if remaining_items > 0:
        return remaining_items * (full_groups + 1)
    else:
        return total_items

# Taking input for total items and group size
total_items_1 = int(input())
total_items_2 = int(input())
group_size = int(input())

# Calculating results using the function
result_1 = calculate_remainder_multiplier(total_items_1, group_size)
result_2 = calculate_remainder_multiplier(total_items_2, group_size)

# Calculating the final product
final_product = result_1 * result_2

# Output the final product
print(final_product)
