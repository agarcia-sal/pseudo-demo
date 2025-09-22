# Define a function mc to calculate additional items needed based on grouping constraints
def mc(total_items, group_size):
    # Calculate how many complete groups can be formed
    complete_groups = total_items // group_size
    remainder = total_items % group_size
    
    # If there is a remainder, calculate total items needed for incomplete groups
    if remainder != 0:
        total_needed = (complete_groups + 1) * remainder
    else:
        # If no remainder, return the original total_items
        total_needed = total_items
    
    return total_needed

# Read input values for two cases and the group size
total_items_for_first_case = int(input())
total_items_for_second_case = int(input())
group_size = int(input())

# Calculate results by calling the mc function for both cases
first_result = mc(total_items_for_first_case, group_size)
second_result = mc(total_items_for_second_case, group_size)

# Output the product of the results from both cases
final_outcome = first_result * second_result
print(final_outcome)
