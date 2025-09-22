def calculate_adjusted_value(total_items, divisor):
    # Calculate the quotient of total_items divided by the divisor
    quotient = total_items // divisor
    # Calculate the remainder of total_items when divided by the divisor
    remainder = total_items % divisor

    # If there are leftover items after grouping
    if remainder > 0:
        # Return the product of the remainder and (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # If no leftover items, return total_items as is
        return total_items

# Main logic starts here
# Read three integers from user input
total_count1 = int(input())
total_count2 = int(input())
group_size = int(input())

# Calculate the adjusted value for total_count1
adjusted_value1 = calculate_adjusted_value(total_count1, group_size)

# Calculate the adjusted value for total_count2
adjusted_value2 = calculate_adjusted_value(total_count2, group_size)

# Calculate the final result by multiplying the two adjusted values
final_result = adjusted_value1 * adjusted_value2

# Print the final result
print(final_result)
