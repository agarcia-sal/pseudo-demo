def calculate_remainder_with_adjustment(total_quantity, segment_size):
    full_segments_count = total_quantity // segment_size
    remaining_quantity = total_quantity % segment_size
    
    if remaining_quantity > 0:
        return remaining_quantity * (full_segments_count + 1)
    else:
        return total_quantity

# Get input from the user
total_items_n, total_items_m, segment_size_s = map(int, input().split())

# Calculate adjusted remainders
adjusted_n = calculate_remainder_with_adjustment(total_items_n, segment_size_s)
adjusted_m = calculate_remainder_with_adjustment(total_items_m, segment_size_s)

# Compute the final output
final_result = adjusted_n * adjusted_m

# Display the result
print(final_result)
