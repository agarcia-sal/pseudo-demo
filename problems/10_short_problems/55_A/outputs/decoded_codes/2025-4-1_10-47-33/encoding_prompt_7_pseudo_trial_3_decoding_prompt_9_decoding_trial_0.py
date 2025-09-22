def check_all_numbers_removed(n):
    # Initialize a list 'is_removed' with 'n' elements, all set to True
    is_removed = [True] * n
    current_index = 0  # Initialize index to 0
    current_step = 1    # Initialize step to 1
    
    # Loop until current_step is greater than 500000
    while current_step <= 500000:
        # If the current index is still marked as True
        if is_removed[current_index]:
            is_removed[current_index] = False  # Mark it as removed
            
        current_step += 1  # Increment the step
        current_index = (current_index + current_step) % n  # Update current index

    # Remaining elements that are still True in is_removed
    remaining = [x for x in is_removed if x]

    # Check if any numbers are still not removed
    if len(remaining) == 0:
        print('YES')  # Output 'YES' if all are removed
    else:
        print('NO')   # Output 'NO' if any are still present
