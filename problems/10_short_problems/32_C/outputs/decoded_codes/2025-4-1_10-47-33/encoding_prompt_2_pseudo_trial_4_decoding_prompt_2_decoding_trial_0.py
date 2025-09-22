# Start the program.

def calculate_remainder_multiplier(total_items, group_size):
    # Divide total_items by group_size to determine full groups
    full_groups = total_items // group_size
    # Find the remainder of total_items divided by group_size
    remaining_items = total_items % group_size
    
    # If there are remaining items
    if remaining_items > 0:
        # Calculate and return the product
        return remaining_items * (full_groups + 1)
    else:
        # Otherwise, return total_items
        return total_items

# Read three integers from input
total_items_1 = int(input())
total_items_2 = int(input())
group_size = int(input())

# Call the function and store results
result_1 = calculate_remainder_multiplier(total_items_1, group_size)
result_2 = calculate_remainder_multiplier(total_items_2, group_size)

# Calculate the product of result_1 and result_2
final_product = result_1 * result_2

# Output the final product
print(final_product)

# End the program.
