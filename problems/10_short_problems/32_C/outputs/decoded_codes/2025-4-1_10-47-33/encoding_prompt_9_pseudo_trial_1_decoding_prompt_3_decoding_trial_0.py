def calculate_adjusted_value(total_items, divisor):
    """
    Calculate the adjusted value based on total_items and divisor.
    If there are leftover items after forming full groups, multiply
    the number of leftover items by the number of full groups plus one.
    Otherwise, return total_items as is.
    """
    quotient = total_items // divisor
    remainder = total_items % divisor

    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_items

# Main logic starts here
total_count1 = int(input())
total_count2 = int(input())
group_size = int(input())

# Calculate adjusted values
adjusted_value1 = calculate_adjusted_value(total_count1, group_size)
adjusted_value2 = calculate_adjusted_value(total_count2, group_size)

# Calculate final result
final_result = adjusted_value1 * adjusted_value2

print(final_result)
