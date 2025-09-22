# Start Program

def mc(total_items, group_size):
    # Calculate complete groups and the remainder
    complete_groups = total_items // group_size
    remainder = total_items % group_size
    
    if remainder != 0:  # If there is a remainder
        # Calculate the additional items needed for incomplete group
        additional_items_needed = (complete_groups + 1) * remainder
        return additional_items_needed
    else:  # If no remainder
        return total_items

# Read input values
total_items_for_first_case = int(input())
total_items_for_second_case = int(input())
group_size = int(input())

# Calculate results
first_result = mc(total_items_for_first_case, group_size)
second_result = mc(total_items_for_second_case, group_size)

# Output the product of the two results
final_outcome = first_result * second_result
print(final_outcome)

# End Program
