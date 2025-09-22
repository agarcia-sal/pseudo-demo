def calculate_adjusted_value(total_items, divisor):
    quotient = total_items // divisor
    remainder = total_items % divisor
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_items

total_count1 = int(input())
total_count2 = int(input())
group_size = int(input())

adjusted_value1 = calculate_adjusted_value(total_count1, group_size)
adjusted_value2 = calculate_adjusted_value(total_count2, group_size)

final_result = adjusted_value1 * adjusted_value2

print(final_result)
