def calculate_remainder_multiplier(total_items, group_size):
    """Calculate the product of remaining items and (full groups + 1) if there are remaining items."""
    
    # Determine how many full groups can be formed
    full_groups = total_items // group_size
    
    # Find remaining items after forming full groups
    remaining_items = total_items % group_size
    
    # If there are remaining items, calculate the product
    if remaining_items > 0:
        return remaining_items * (full_groups + 1)
    
    # If no remaining items, return the total items
    return total_items

# Read three integers from input
total_items_1 = int(input())
total_items_2 = int(input())
group_size = int(input())

# Compute results using the defined function
result_1 = calculate_remainder_multiplier(total_items_1, group_size)
result_2 = calculate_remainder_multiplier(total_items_2, group_size)

# Calculate the product of result_1 and result_2
final_product = result_1 * result_2

# Output the final product
print(final_product)
