def calculate_adjustment(total_items, group_size):
    # Determine how many complete groups can be formed
    full_groups = total_items // group_size
    
    # Calculate the number of leftover items
    leftover_items = total_items % group_size
    
    # If there are leftover items, adjust total_items accordingly
    if leftover_items:
        return total_items + leftover_items * (full_groups + 1)
    else:
        return total_items  # Return total_items if no adjustment is needed

# Read input values for total_items (n), another total_items (m), and group_size (s)
n = int(input())
m = int(input())
s = int(input())

# Calculate adjusted values for the first set of items (n)
adjusted_value_n = calculate_adjustment(n, s)

# Calculate adjusted values for the second total of items (m)
adjusted_value_m = calculate_adjustment(m, s)

# Calculate the final product of adjusted_value_n and adjusted_value_m
final_product = adjusted_value_n * adjusted_value_m

# Print the final product
print(final_product)
