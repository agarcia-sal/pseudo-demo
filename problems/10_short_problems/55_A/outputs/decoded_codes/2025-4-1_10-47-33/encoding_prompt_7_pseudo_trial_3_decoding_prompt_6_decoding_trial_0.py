def check_all_numbers_removed(n):
    # Initialize a list 'is_removed' with 'n' elements, all set to True
    is_removed = [True] * n
    # Initialize index 'current_index' to 0
    current_index = 0
    # Initialize step 'current_step' to 1
    current_step = 1

    # While current_step is less than or equal to 500000
    while current_step <= 500000:
        # If is_removed[current_index] is True
        if is_removed[current_index]:
            # Mark is_removed[current_index] as False
            is_removed[current_index] = False
        
        # Increment current_step by 1
        current_step += 1
        # Update current_index to (current_index + current_step) MOD n
        current_index = (current_index + current_step) % n

    # Initialize list 'remaining' containing elements from is_removed that are still True
    remaining = [x for x in is_removed if x]

    # If length of remaining is 0 then
    if len(remaining) == 0:
        # Print 'YES'
        print('YES')
    else:
        # Else print 'NO'
        print('NO')

# Example usage:
n = int(input())  # Read input for the total number of elements
check_all_numbers_removed(n)
