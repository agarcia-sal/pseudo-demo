def check_boolean_list():
    # Step 2: Receive Input
    list_size = int(input())  # User input for the size of the list
    
    # Step 3: Initialize Boolean List
    boolean_list = [True] * list_size  # Create a list with all elements set to True
    
    # Step 4: Initialize Iteration Variables
    current_index = 0
    step = 1
    
    # Step 5: Loop through iterations
    while step <= 500000:
        if boolean_list[current_index]:  # Check current boolean value
            boolean_list[current_index] = False  # Set it to False
            
        # Increment step and update current_index for the next iteration
        step += 1
        current_index = (current_index + step) % list_size  # Wrap around using modulo
        
    # Step 6: Check Remaining True Values
    remaining_true = [value for value in boolean_list if value]  # Filter for True values
    
    # Step 7: Output Result
    if len(remaining_true) == 0:
        print("YES")  # All elements set to False
    else:
        print("NO")   # Some elements remain True

# Call the function to execute the algorithm
check_boolean_list()
