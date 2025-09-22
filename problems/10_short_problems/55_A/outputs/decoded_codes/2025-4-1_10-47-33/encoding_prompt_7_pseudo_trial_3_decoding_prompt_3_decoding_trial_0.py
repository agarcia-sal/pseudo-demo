def check_all_numbers_removed(n):
    # Initialize the list 'is_removed' with 'n' elements, all set to True
    is_removed = [True] * n
    current_index = 0  # Initialize index to 0
    current_step = 1    # Initialize step to 1
    
    # Continue until current_step exceeds 500000
    while current_step <= 500000:
        # Mark the current index as removed if it is still True
        if is_removed[current_index]:
            is_removed[current_index] = False
        
        # Move to the next step
        current_step += 1
        
        # Update current_index using modulo n to wrap around
        current_index = (current_index + current_step) % n
    
    # Filter remaining elements that are still True in is_removed
    remaining = [x for x in is_removed if x]
    
    # Print results based on whether any elements are still True
    if len(remaining) == 0:
        print('YES')
    else:
        print('NO')

# Example usage:
# n = int(input())
# check_all_numbers_removed(n)
