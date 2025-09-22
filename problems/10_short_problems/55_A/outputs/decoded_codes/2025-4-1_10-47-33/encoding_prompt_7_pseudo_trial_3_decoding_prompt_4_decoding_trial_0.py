def check_all_numbers_removed(n):
    # Initialize a list 'is_removed' with 'n' elements, all set to True
    is_removed = [True] * n
    current_index = 0
    current_step = 1

    # Process steps until reaching 500000
    while current_step <= 500000:
        if is_removed[current_index]:
            # Mark the current index as removed
            is_removed[current_index] = False
        
        # Prepare for the next step
        current_step += 1
        current_index = (current_index + current_step) % n  # Update current_index
    
    # Extract remaining numbers that are still marked as True
    remaining = [removed for removed in is_removed if removed]
    
    # Print 'YES' if all numbers are removed, otherwise print 'NO'
    if not remaining:
        print('YES')
    else:
        print('NO')

# Example usage:
n = int(input())
check_all_numbers_removed(n)
