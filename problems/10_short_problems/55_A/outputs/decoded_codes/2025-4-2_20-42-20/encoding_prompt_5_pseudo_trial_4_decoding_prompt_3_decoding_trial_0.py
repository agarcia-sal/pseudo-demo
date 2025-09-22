def elimination_process():
    # Step 1: Read the size of the list
    n = int(input())
    
    # Step 2: Initialize the status list with True values
    status = [True] * n
    current_position = 0
    increment = 1
    
    # Step 3: Start the elimination process
    while increment <= 500000:
        if status[current_position]:  # If the position is still active
            status[current_position] = False  # Mark as inactive
        
        increment += 1  # Increment the count
        current_position = (current_position + increment) % n  # Move to the next position

    # Step 4: Check the remaining active positions
    active_positions = [pos for pos in status if pos]  # Create list of active positions
    if len(active_positions) == 0:  # If there are no active positions
        print("YES")  # Successful elimination
    else:
        print("NO")  # There are still active positions

# Call the function to execute the elimination process
elimination_process()
