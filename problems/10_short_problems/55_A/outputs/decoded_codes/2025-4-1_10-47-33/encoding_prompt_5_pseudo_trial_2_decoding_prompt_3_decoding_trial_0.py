def elimination_process():
    # Step 1: Get the size of the list from user input
    n = int(input())
    
    # Step 2: Initialize the boolean list with True values
    boolean_list = [True] * n
    
    # Step 3: Set up the counters
    outer_counter = 1
    inner_counter = 0

    # Step 4: Elimination loop
    while outer_counter <= 500000:
        if boolean_list[inner_counter]:  # Check if the current element is True
            boolean_list[inner_counter] = False  # Mark as eliminated

        outer_counter += 1  # Increment the outer counter
        # Update the inner counter, wrapping around using modulus
        inner_counter = (inner_counter + outer_counter) % n

    # Step 5: Check remaining values
    remaining_true_values = [value for value in boolean_list if value]

    # Step 6: Determine the result and print 'YES' or 'NO'
    if len(remaining_true_values) == 0:
        print('YES')  # All values have been eliminated
    else:
        print('NO')   # Some values are still True

# Call the function to run the program
elimination_process()
