# Function to calculate remaining items and the multiplier based on full groups
def calculate_remainder_multiplier(total_items, group_size):
    # Determine how many full groups can be made
    full_groups = total_items // group_size
    # Find the remainder items when total_items is divided by group_size
    remaining_items = total_items % group_size
    
    # If there are remaining items, calculate the product of remaining_items and (full_groups + 1)
    if remaining_items > 0:
        return remaining_items * (full_groups + 1)
    else:
        # Return the total_items if perfectly divisible
        return total_items

# Read three integers from input
total_items_1 = int(input())
total_items_2 = int(input())
group_size = int(input())

# Call the function with total_items_1
result_1 = calculate_remainder_multiplier(total_items_1, group_size)

# Call the function with total_items_2
result_2 = calculate_remainder_multiplier(total_items_2, group_size)

# Calculate the product of result_1 and result_2
final_product = result_1 * result_2

# Output the final product
print(final_product)
