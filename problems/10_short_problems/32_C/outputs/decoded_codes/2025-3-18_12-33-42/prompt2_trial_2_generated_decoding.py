def calculate_remainder(total, group_size):
    complete_groups = total // group_size  # Calculate how many complete groups can be formed
    remaining_items = total % group_size    # Calculate the remaining items after complete groups

    if remaining_items > 0:                  # Check if there are remaining items
        return remaining_items * (complete_groups + 1)  # Calculate the product as per the condition
    else:
        return total                          # Return total if no remaining items

# Take input from the user
total_items_1 = int(input())
total_items_2 = int(input())
group_size = int(input())

# Compute remainders using the calculate_remainder function
remainder_1 = calculate_remainder(total_items_1, group_size)
remainder_2 = calculate_remainder(total_items_2, group_size)

# Output the product of the two remainder values
print(remainder_1 * remainder_2)
