def check_if_all_false(n):
    """
    Checks if all values in a boolean list of size n have been set to False
    after a series of operations specified by a step incrementing mechanism.

    :param n: Integer representing the size of the boolean list.
    """
    # Initialize a boolean list of size n with all values set to True
    boolean_list = [True] * n
    index = 0
    step = 1

    # Continue iterating while step is less than or equal to 500,000
    while step <= 500000:
        # If the current position in the boolean_list is True
        if boolean_list[index]:
            # Set the current position to False
            boolean_list[index] = False

        # Increment step for the next iteration
        step += 1
        
        # Update index using circular indexing based on step
        index = (index + step) % n

    # Filter the boolean list to find all remaining True values
    remaining_true = [value for value in boolean_list if value]

    # Print 'YES' if there are no True values remaining, else print 'NO'
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Example usage (not part of the implementation)
n = int(input())
check_if_all_false(n)
