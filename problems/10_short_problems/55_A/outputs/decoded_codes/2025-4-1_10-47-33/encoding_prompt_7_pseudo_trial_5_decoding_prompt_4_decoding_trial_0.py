def check_if_all_false(n):
    """
    Check if all values in a boolean list of size n can be set to False after processing.
    
    :param n: An integer indicating the size of the boolean list.
    """
    # Initialize a list of boolean values all set to True
    boolean_list = [True] * n
    index = 0
    step = 1

    # Iterate while step is less than or equal to 500000
    while step <= 500000:
        # If the current position in the boolean_list is True
        if boolean_list[index]:
            # Set the current position to False
            boolean_list[index] = False
        
        # Increment step for the next iteration
        step += 1

        # Update index using circular indexing based on step
        index = (index + step) % n

    # Check how many True values remain in the boolean_list
    remaining_true = [value for value in boolean_list if value]

    # If there are no True values remaining, print 'YES'
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Example invocation (Uncomment to use)
# n = int(input())
# check_if_all_false(n)
