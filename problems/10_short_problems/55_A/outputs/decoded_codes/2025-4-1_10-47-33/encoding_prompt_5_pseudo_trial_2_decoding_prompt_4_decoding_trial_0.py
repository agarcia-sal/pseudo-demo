def elimination_process():
    # Step 1: Get the size of the list from user input
    n = int(input())
    
    # Step 2: Initialize a list with n elements, all set to True
    boolean_list = [True] * n
    
    # Step 3: Initialize counters for the elimination process
    outer_counter = 1
    inner_counter = 0
    
    # Step 4: Elimination loop
    while outer_counter <= 500000:
        # Check if the current index in the boolean list is True
        if boolean_list[inner_counter]:
            boolean_list[inner_counter] = False  # Eliminate
        outer_counter += 1
        inner_counter = (inner_counter + outer_counter) % n  # Update index within bounds of boolean_list
    
    # Step 5: Create a list of remaining True values
    remaining_true_values = [value for value in boolean_list if value]
    
    # Step 6: Determine the result based on the remaining True values
    if len(remaining_true_values) == 0:
        print('YES')  # All values have been eliminated
    else:
        print('NO')   # Some values are still True

# Calling the function to run the elimination process
elimination_process()
