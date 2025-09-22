def calculate_remainder_multiplier(total_items, group_size):
    # Calculate the number of full groups
    full_groups = total_items // group_size
    
    # Calculate remaining items after forming full groups
    remaining_items = total_items % group_size
    
    # If there are remaining items, calculate the product
    if remaining_items > 0:
        return remaining_items * (full_groups + 1)
    else:
        return total_items

# Read inputs
total_items_1 = int(input())
total_items_2 = int(input())
group_size = int(input())

# Call the function for both sets of total items
result_1 = calculate_remainder_multiplier(total_items_1, group_size)
result_2 = calculate_remainder_multiplier(total_items_2, group_size)

# Calculate the final product
final_product = result_1 * result_2

# Output the final product
print(final_product)
