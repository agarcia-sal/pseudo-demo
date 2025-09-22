def calculate_adjusted_value(total_items, group_size):
    # Calculate the number of full groups and any remaining items
    full_groups = total_items // group_size
    remaining_items = total_items % group_size
    
    # Determine the adjusted value based on remaining items
    if remaining_items > 0:
        return remaining_items * (full_groups + 1)
    else:
        return total_items

# Read input values
total_items1 = int(input())
total_items2 = int(input())
group_size = int(input())

# Calculate adjusted values for both inputs
result1 = calculate_adjusted_value(total_items1, group_size)
result2 = calculate_adjusted_value(total_items2, group_size)

# Calculate and print the final output
final_output = result1 * result2
print(final_output)
