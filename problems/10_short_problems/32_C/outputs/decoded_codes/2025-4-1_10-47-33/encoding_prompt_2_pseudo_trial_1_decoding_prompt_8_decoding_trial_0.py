def mc(total_items, group_size):
    complete_groups = total_items // group_size
    remainder = total_items % group_size

    if remainder > 0:
        needed_items = (complete_groups + 1) * remainder
        return total_items + needed_items
    else:
        return total_items

# Read input values
total_items_for_first_case, total_items_for_second_case, group_size = map(int, input().split())

# Calculate results
first_result = mc(total_items_for_first_case, group_size)
second_result = mc(total_items_for_second_case, group_size)

# Output
final_outcome = first_result * second_result
print(final_outcome)
