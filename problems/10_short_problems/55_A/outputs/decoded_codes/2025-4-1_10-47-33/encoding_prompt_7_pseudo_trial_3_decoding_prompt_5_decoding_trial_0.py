def check_all_numbers_removed(n):
    # Initialize a list to track removed status for each index
    is_removed = [True] * n
    current_index = 0
    current_step = 1
    
    # Loop for processing up to 500,000 steps
    while current_step <= 500000:
        # Mark the current index as removed (set to False)
        if is_removed[current_index]:
            is_removed[current_index] = False
        
        # Increment the current step for the next iteration
        current_step += 1
        # Update current index based on current step
        current_index = (current_index + current_step) % n
    
    # Get the remaining elements that are still marked as True
    remaining = [index for index, removed in enumerate(is_removed) if removed]
    
    # Print 'YES' if no elements are remaining, else 'NO'
    if len(remaining) == 0:
        print('YES')
    else:
        print('NO')

# Example usage (you can uncomment to test):
# n = int(input())
# check_all_numbers_removed(n)
