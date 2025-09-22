def manage_active_elements():
    # Step 1: Accept input for the number of elements
    number_of_elements = int(input())
    
    # Step 2: Initialize a list indicating whether elements are active
    is_active = [True] * number_of_elements
    
    # Step 3: Initialize the variables for iteration
    index = 0
    step = 1

    # Step 4: Loop until the step exceeds the limit
    while step <= 500000:
        # Step 4a: Check if the current index is active
        if is_active[index]:
            # Mark this index as inactive
            is_active[index] = False
        
        # Step 4b: Increment the step
        step += 1
        
        # Step 4c: Update the index based on the current step
        index = (index + step) % number_of_elements  # Calculate new index

    # Step 5: Create a list of active elements
    active_elements = [i for i in is_active if i]  # Collecting True values

    # Step 6: Check if there are any active elements left
    if not active_elements:
        print('YES')  # Indicating no active elements remaining
    else:
        print('NO')   # Indicating there are active elements remaining

# Run the function
manage_active_elements()
