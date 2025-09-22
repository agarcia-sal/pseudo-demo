def check_if_all_false(n):
    # INPUT: An integer n indicating the size of a boolean list
    # OUTPUT: Prints 'YES' if all values in the list are False; otherwise, prints 'NO'

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

    # Filter the boolean_list to find all remaining True values
    remaining_true = [value for value in boolean_list if value]

    # If there are no True values remaining
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Example usage:
# To call the function, uncomment the line below and provide an integer value.
# check_if_all_false(int(input()))
