def mc(total_items, group_size):
    # Calculate the number of complete groups that can be formed
    complete_groups = total_items // group_size
    remainder = total_items % group_size
    
    if remainder > 0:
        # If there are items that don't fit into a complete group,
        # calculate the additional items needed for the next group
        additional_items_needed = (complete_groups + 1) * remainder
        return additional_items_needed
    else:
        # If there is no remainder, return the original number of total_items
        return total_items

# Read input values for both cases and the group size
total_items_for_first_case = int(input())
total_items_for_second_case = int(input())
group_size = int(input())

# Calculate results using the mc function
first_result = mc(total_items_for_first_case, group_size)
second_result = mc(total_items_for_second_case, group_size)

# Output the product of the results from both cases
final_outcome = first_result * second_result
print(final_outcome)
