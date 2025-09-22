def calculate_groups(total_items, group_size):
    # Calculate the number of full groups that can be formed
    number_of_groups = total_items // group_size  # Floor division to get full groups
    remainder = total_items % group_size  # Calculate remainder items

    # If there is a remainder, increase the count of groups by one
    if remainder > 0:
        return number_of_groups + 1  # Include the extra group for remaining items
    else:
        return number_of_groups  # No extra group needed

# Read three integers from user input
total_items_a = int(input())  # Quantity of items A
total_items_b = int(input())  # Quantity of items B
group_size = int(input())  # Size of each group

# Calculate the number of groups for each quantity
groups_a = calculate_groups(total_items_a, group_size)
groups_b = calculate_groups(total_items_b, group_size)

# Calculate the product of groups formed from both quantities
result = groups_a * groups_b

# Output the final result
print(result)
