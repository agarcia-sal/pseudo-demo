# Start Program

def calculate_remainder_with_adjustment(total_quantity, segment_size):
    # Calculate how many full segments fit into total_quantity
    full_segments_count = total_quantity // segment_size
    # Calculate the remaining quantity after fitting those full segments
    remaining_quantity = total_quantity % segment_size
    
    # Check if there is any remainder
    if remaining_quantity > 0:
        # Return the product of remaining_quantity and one more than full_segments_count
        return remaining_quantity * (full_segments_count + 1)
    else:
        # Return total_quantity as is if no remainder
        return total_quantity

# Get Input
total_items_n, total_items_m, segment_size_s = map(int, input().split())

# Calculate Adjusted Remainders
adjusted_n = calculate_remainder_with_adjustment(total_items_n, segment_size_s)
adjusted_m = calculate_remainder_with_adjustment(total_items_m, segment_size_s)

# Compute Final Output
final_result = adjusted_n * adjusted_m

# Display the Result
print(final_result)

# End Program
