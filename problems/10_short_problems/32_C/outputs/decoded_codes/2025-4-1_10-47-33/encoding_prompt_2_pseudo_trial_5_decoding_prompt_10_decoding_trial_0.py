def calculate_remainder_with_adjustment(total_quantity, segment_size):
    """Calculate the adjusted remainder based on total quantity and segment size."""
    full_segments_count = total_quantity // segment_size
    remaining_quantity = total_quantity % segment_size
    
    if remaining_quantity > 0:
        # This accounts for the leftover items needing adjustment
        return remaining_quantity * (full_segments_count + 1)
    
    return total_quantity  # Return total quantity if there are no remainders


def main():
    # Get input values
    total_items_n, total_items_m, segment_size_s = map(int, input().split())
    
    # Calculate adjusted remainders
    adjusted_n = calculate_remainder_with_adjustment(total_items_n, segment_size_s)
    adjusted_m = calculate_remainder_with_adjustment(total_items_m, segment_size_s)
    
    # Compute the final output
    final_result = adjusted_n * adjusted_m
    
    # Display the result
    print(final_result)


if __name__ == "__main__":
    main()
