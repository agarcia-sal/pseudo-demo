# Define the function to calculate adjusted total items based on grouping
def mc(total_items, group_size):
    # Calculate number of complete groups and remainder
    complete_groups = total_items // group_size
    remainder = total_items % group_size
    
    # If there is a remainder, calculate extra items needed
    if remainder > 0:
        additional_items_needed = (complete_groups + 1) * remainder
        return additional_items_needed
    else:
        # If perfectly grouped, return original total items
        return total_items

# Read input values and convert to integers
total_items_for_first_case = int(input())
total_items_for_second_case = int(input())
group_size = int(input())

# Calculate results by calling the mc function
first_result = mc(total_items_for_first_case, group_size)
second_result = mc(total_items_for_second_case, group_size)

# Output the product of the two results
final_outcome = first_result * second_result
print(final_outcome)
