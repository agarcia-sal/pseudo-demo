def calculate_groups(total_items, group_size):
    # Calculate the number of full groups and the remainder
    number_of_groups = total_items // group_size
    remainder = total_items % group_size
    
    # If there is a remainder, increment the group count by one
    if remainder > 0:
        return number_of_groups + 1  # Include additional group for remaining items
    else:
        return number_of_groups  # No additional group needed

# Read three integers from user input
total_items_a = int(input())
total_items_b = int(input())
group_size = int(input())

# Calculate the number of groups for each quantity
groups_a = calculate_groups(total_items_a, group_size)
groups_b = calculate_groups(total_items_b, group_size)

# Calculate the product of groups formed from both quantities
result = groups_a * groups_b

# Output the final result
print(result)
