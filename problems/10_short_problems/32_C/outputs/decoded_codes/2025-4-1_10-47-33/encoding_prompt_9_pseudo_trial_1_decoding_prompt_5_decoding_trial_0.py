def calculate_adjusted_value(total_items, divisor):
    # Calculate the quotient
    quotient = total_items // divisor
    # Calculate the remainder
    remainder = total_items % divisor
    
    # If there are leftover items
    if remainder > 0:
        # Return the product of remainder and (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # Otherwise, return total_items as is
        return total_items

# Main logic
# Read inputs from user
total_count1 = int(input())
total_count2 = int(input())
group_size = int(input())

# Calculate the adjusted values for both item counts
adjusted_value1 = calculate_adjusted_value(total_count1, group_size)
adjusted_value2 = calculate_adjusted_value(total_count2, group_size)

# Calculate final result
final_result = adjusted_value1 * adjusted_value2

# Print the final result
print(final_result)
