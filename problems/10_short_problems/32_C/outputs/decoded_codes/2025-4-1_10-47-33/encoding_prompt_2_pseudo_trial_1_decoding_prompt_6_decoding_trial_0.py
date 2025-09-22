# Define a function to calculate the adjusted total items based on groups
def calculate_groups(total_items, group_size):
    # Calculate complete groups and remainder
    complete_groups = total_items // group_size
    remainder = total_items % group_size
    
    # Check if there is a remainder
    if remainder > 0:
        # Calculate items needed for incomplete groups
        total_needed = (complete_groups + 1) * remainder
    else:
        # No remainder, return the original total
        total_needed = total_items
    
    return total_needed

# Read input values and convert to integers
total_items_first_case, total_items_second_case, group_size = map(int, input().split())

# Calculate results by calling the function
first_result = calculate_groups(total_items_first_case, group_size)
second_result = calculate_groups(total_items_second_case, group_size)

# Multiply the results and print the final outcome
final_result = first_result * second_result
print(final_result)
