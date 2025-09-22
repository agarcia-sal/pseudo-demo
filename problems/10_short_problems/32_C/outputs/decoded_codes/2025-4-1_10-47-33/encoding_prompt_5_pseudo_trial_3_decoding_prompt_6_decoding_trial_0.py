def calculate_groups(total_items, group_size):
    # Calculate the number of full groups and the remainder
    number_of_groups = total_items // group_size  # Integer division to get the number of complete groups
    remainder = total_items % group_size           # Remainder after forming groups
    
    # If there is a remainder, increase the group count by one
    if remainder > 0:
        return number_of_groups + 1  # Include the extra group for remaining items
    else:
        return number_of_groups  # No extra group needed

# Read three integers from user input
total_items_a = int(input())  # Read total items of the first quantity
total_items_b = int(input())  # Read total items of the second quantity
group_size = int(input())      # Read the size of the group

# Calculate the number of groups for each quantity
groups_a = calculate_groups(total_items_a, group_size)
groups_b = calculate_groups(total_items_b, group_size)

# Calculate the product of groups formed from both quantities
result = groups_a * groups_b

# Output the final result
print(result)
