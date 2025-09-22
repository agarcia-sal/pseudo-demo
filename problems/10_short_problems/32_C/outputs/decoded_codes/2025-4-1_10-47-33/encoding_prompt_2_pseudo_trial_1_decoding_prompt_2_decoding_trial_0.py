# Start Program

# Define function mc with parameters total_items and group_size
def mc(total_items, group_size):
    complete_groups = total_items // group_size
    remainder = total_items % group_size
    
    if remainder > 0:
        # Calculate total items for incomplete groups
        total_needed = (complete_groups + 1) * remainder
    else:
        # Return the original number of total_items
        total_needed = total_items
    
    return total_needed

# Read input values
total_items_for_first_case, total_items_for_second_case, group_size = map(int, input().split())

# Calculate results
first_result = mc(total_items_for_first_case, group_size)
second_result = mc(total_items_for_second_case, group_size)

# Output
final_outcome = first_result * second_result
print(final_outcome)

# End Program
