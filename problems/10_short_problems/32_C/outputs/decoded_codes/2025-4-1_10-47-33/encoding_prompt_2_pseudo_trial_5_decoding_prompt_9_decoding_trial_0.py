def calculate_remainder_with_adjustment(total_quantity, segment_size):
    # Calculate how many full segments fit into the total quantity
    full_segments_count = total_quantity // segment_size
    # Calculate the remaining quantity after full segments
    remaining_quantity = total_quantity % segment_size
    
    # If there is any remainder, adjust the return value
    if remaining_quantity > 0:
        return remaining_quantity * (full_segments_count + 1)
    else:
        return total_quantity  # No adjustment needed

# Get input from the user
input_values = input().strip().split()
total_items_n = int(input_values[0])
total_items_m = int(input_values[1])
segment_size_s = int(input_values[2])

# Calculate adjusted remainders
adjusted_n = calculate_remainder_with_adjustment(total_items_n, segment_size_s)
adjusted_m = calculate_remainder_with_adjustment(total_items_m, segment_size_s)

# Compute final output
final_result = adjusted_n * adjusted_m

# Display the result
print(final_result)
