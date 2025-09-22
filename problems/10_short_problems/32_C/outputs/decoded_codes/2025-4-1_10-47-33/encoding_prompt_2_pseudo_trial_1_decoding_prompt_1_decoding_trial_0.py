# Start Program

def mc(total_items, group_size):
    # Calculate how many complete groups and the remainder
    complete_groups = total_items // group_size
    remainder = total_items % group_size

    # Conditional check for remainder
    if remainder != 0:  # If there is a remainder
        # Calculate total items needed
        total_needed = (complete_groups + 1) * remainder
        return total_needed
    else:  # If there is no remainder
        return total_items

# Read input values
total_items_for_first_case, total_items_for_second_case, group_size = map(int, input().split())

# Calculate results
first_result = mc(total_items_for_first_case, group_size)
second_result = mc(total_items_for_second_case, group_size)

# Output
final_outcome = first_result * second_result
print(final_outcome)

# End Program
