def calculate_remainder_with_adjustment(total_quantity, segment_size):
    # Calculate how many full segments fit into total_quantity
    full_segments_count = total_quantity // segment_size
    
    # Calculate the remaining quantity after fitting those full segments
    remaining_quantity = total_quantity % segment_size

    # If there is any remainder, adjust the count
    if remaining_quantity > 0:
        return remaining_quantity * (full_segments_count + 1)
    
    # No remainder, return total_quantity as is
    return total_quantity


# Read inputs from the user
total_items_n = int(input())
total_items_m = int(input())
segment_size_s = int(input())

# Calculate Adjusted Remainders for both total_items_n and total_items_m
adjusted_n = calculate_remainder_with_adjustment(total_items_n, segment_size_s)
adjusted_m = calculate_remainder_with_adjustment(total_items_m, segment_size_s)

# Compute Final Output
final_result = adjusted_n * adjusted_m

# Display the Result
print(final_result)
