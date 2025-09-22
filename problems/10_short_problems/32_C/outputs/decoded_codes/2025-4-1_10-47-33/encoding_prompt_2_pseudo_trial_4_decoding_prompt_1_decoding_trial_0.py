# Step 1: Start the program (implied in Python as the code execution begins here)

# Step 2: Define a function named "calculate_remainder_multiplier"
def calculate_remainder_multiplier(total_items, group_size):
    # Divide total_items by group_size to find full_groups
    full_groups = total_items // group_size
    # Find the remainder
    remaining_items = total_items % group_size
    
    # Check if there are remaining items
    if remaining_items > 0:
        # Calculate and return the product
        return remaining_items * (full_groups + 1)
    else:
        # Return total_items when no remaining items are left
        return total_items

# Step 3: Read three integers from input
total_items_1 = int(input())
total_items_2 = int(input())
group_size = int(input())

# Step 4: Call the function with total_items_1 and group_size
result_1 = calculate_remainder_multiplier(total_items_1, group_size)

# Step 5: Call the function with total_items_2 and group_size
result_2 = calculate_remainder_multiplier(total_items_2, group_size)

# Step 6: Calculate the product of result_1 and result_2
final_product = result_1 * result_2

# Step 7: Output the final product
print(final_product)

# Step 8: End the program (implied, as the program terminates)
