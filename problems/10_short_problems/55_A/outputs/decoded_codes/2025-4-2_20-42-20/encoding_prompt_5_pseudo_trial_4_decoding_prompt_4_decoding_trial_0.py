def elimination_process():
    # Initialize the variables
    n = int(input())  # Read integer value for the size of the list
    status = [True] * n  # Create a list with n True values, indicating active positions
    current_position = 0  # Starting position for the elimination process
    increment = 1  # Starting increment value

    # Start the elimination process
    while increment <= 500000:
        # Check the current position status
        if status[current_position]:  # If the position is active
            status[current_position] = False  # Mark it as inactive
        # Increment for the next iteration
        increment += 1
        # Update the current position using modulo to wrap around
        current_position = (current_position + increment) % n

    # Check the remaining active positions
    active_positions = [pos for pos in status if pos]  # Create a list of active positions

    # Determine if all positions are inactive
    if len(active_positions) == 0:
        print("YES")  # All positions are inactive
    else:
        print("NO")  # There are still active positions

# Call the function to execute the elimination process
elimination_process()
