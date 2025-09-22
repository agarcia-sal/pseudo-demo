def calculate_remainder_multiplier(total_items, group_size):
    full_groups = total_items // group_size
    remaining_items = total_items % group_size
    
    if remaining_items > 0:
        return remaining_items * (full_groups + 1)
    else:
        return total_items

total_items_1 = int(input())
total_items_2 = int(input())
group_size = int(input())

result_1 = calculate_remainder_multiplier(total_items_1, group_size)
result_2 = calculate_remainder_multiplier(total_items_2, group_size)

final_product = result_1 * result_2

print(final_product)
