def calculate_groups(total_items, group_size):
    number_of_groups = total_items // group_size
    remainder = total_items % group_size
    
    if remainder > 0:
        return number_of_groups + 1
    else:
        return number_of_groups

total_items_a = int(input())
total_items_b = int(input())
group_size = int(input())

groups_a = calculate_groups(total_items_a, group_size)
groups_b = calculate_groups(total_items_b, group_size)

result = groups_a * groups_b

print(result)
