def eliminate_positions():
    # Step 1: Read integer n, representing the size of the list
    n = int(input())
    
    # Step 2: Initialize the status list with True values
    status = [True] * n
    
    current_position = 0  # Starting position
    increment = 1         # Initial increment value

    # Step 3: Start the elimination process
    while increment <= 500000:
        # If the current position is active
        if status[current_position]:
            # Mark as inactive
            status[current_position] = False
        
        increment += 1  # Increment by 1
        current_position = (current_position + increment) % n  # Move to the next position, wrapping around if necessary

    # Step 4: Check the remaining active positions
    active_positions = [pos for pos in status if pos]  # List of active positions

    # Output result based on the number of active positions
    if len(active_positions) == 0:  # If all positions are inactive
        print("YES")
    else:
        print("NO")

# Call the function to execute
eliminate_positions()
