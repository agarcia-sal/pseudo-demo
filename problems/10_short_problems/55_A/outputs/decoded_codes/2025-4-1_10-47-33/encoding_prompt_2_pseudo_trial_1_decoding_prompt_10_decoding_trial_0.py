def elimination_process():
    # Step 1: Initialize Input
    number_of_elements = int(input())
    
    # Step 2: Create a Boolean List
    is_active = [True] * number_of_elements

    # Step 3: Set Initial Indices
    current_index = 0
    step_size = 1

    # Step 4: Start Elimination Process
    while step_size <= 500000:
        if is_active[current_index]:  # Check if the current index is active
            is_active[current_index] = False  # Eliminate the current position
            
        # Update step size and current index for the next round
        step_size += 1
        current_index = (current_index + step_size) % number_of_elements  # Wrap around

    # Step 5: Check Remaining Active Entries
    remaining_active = [active for active in is_active if active]

    # Step 6: Determine and Print Final Result
    if len(remaining_active) == 0:
        print("YES")  # All positions have been eliminated
    else:
        print("NO")   # Some positions are still active

# Call the function to execute the elimination process
elimination_process()
