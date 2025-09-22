def calculate_remainder_with_adjustment(total_quantity, segment_size):
    # Calculate how many full segments fit into total_quantity
    full_segments_count = total_quantity // segment_size
    # Calculate the remaining quantity after full segments
    remaining_quantity = total_quantity % segment_size
    
    # If there is any remainder, calculate the adjusted value
    if remaining_quantity > 0:
        return remaining_quantity * (full_segments_count + 1)
    else:
        return total_quantity

# Get input from the user
total_items_n, total_items_m, segment_size_s = map(int, input().split())

# Calculate adjusted remainders for both items
adjusted_n = calculate_remainder_with_adjustment(total_items_n, segment_size_s)
adjusted_m = calculate_remainder_with_adjustment(total_items_m, segment_size_s)

# Compute final output
final_result = adjusted_n * adjusted_m

# Display the result
print(final_result)
