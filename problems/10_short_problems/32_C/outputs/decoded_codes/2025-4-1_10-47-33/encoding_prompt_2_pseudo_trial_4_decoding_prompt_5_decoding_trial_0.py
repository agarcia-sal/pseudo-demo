def calculate_remainder_multiplier(total_items, group_size):
    # Determine how many full groups can be made
    full_groups = total_items // group_size
    # Find the remainder when total_items is divided by group_size
    remaining_items = total_items % group_size
    
    # If there are remaining items, calculate the product
    if remaining_items > 0:
        return remaining_items * (full_groups + 1)
    else:
        return total_items

# Read three integers from input
total_items_1 = int(input())
total_items_2 = int(input())
group_size = int(input())

# Call the function and store the results
result_1 = calculate_remainder_multiplier(total_items_1, group_size)
result_2 = calculate_remainder_multiplier(total_items_2, group_size)

# Calculate the product of the results
final_product = result_1 * result_2

# Output the final product
print(final_product)
