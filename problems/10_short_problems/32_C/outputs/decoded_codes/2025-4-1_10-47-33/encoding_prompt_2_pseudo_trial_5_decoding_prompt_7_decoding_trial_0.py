# Start Program

def calculate_remainder_with_adjustment(total_quantity, segment_size):
    # Calculate how many full segments fit into total_quantity
    full_segments_count = total_quantity // segment_size
    
    # Calculate the remaining quantity after fitting full segments
    remaining_quantity = total_quantity % segment_size
    
    # Check if there is a remainder
    if remaining_quantity > 0:
        # If there is a remainder, adjust and return the product
        return remaining_quantity * (full_segments_count + 1)
    else:
        # If there is no remainder, return total_quantity as is
        return total_quantity

# Get input
# The input will be split into three integer values
total_items_n, total_items_m, segment_size_s = map(int, input().split())

# Calculate adjusted remainders
adjusted_n = calculate_remainder_with_adjustment(total_items_n, segment_size_s)
adjusted_m = calculate_remainder_with_adjustment(total_items_m, segment_size_s)

# Compute the final output
final_result = adjusted_n * adjusted_m

# Display the result
print(final_result)

# End Program
