def calculate_remainder_adjusted_count(total_items, group_size):
    # Calculate quotient and remainder
    quotient, remainder = divmod(total_items, group_size)
    
    # Check if the remainder is greater than zero
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_items

# Read input values from the user
total_items_n = int(input())
total_items_m = int(input())
group_size = int(input())

# Call the function for total_items_n and total_items_m
count_n = calculate_remainder_adjusted_count(total_items_n, group_size)
count_m = calculate_remainder_adjusted_count(total_items_m, group_size)

# Calculate the final result as the product of count_n and count_m
final_result = count_n * count_m

# Output the final result
print(final_result)
