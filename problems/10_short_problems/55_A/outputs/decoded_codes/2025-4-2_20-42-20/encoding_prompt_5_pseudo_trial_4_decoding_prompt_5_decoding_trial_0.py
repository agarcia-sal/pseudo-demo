# Function to determine if all positions can be marked inactive
def elimination_process():
    # Step 1: Read the size of the list
    n = int(input())
    
    # Step 2: Initialize the status list with True values
    status = [True] * n  # All positions are initially active
    current_position = 0  # Start at the first position
    increment = 1  # Start incrementing from 1

    # Step 3: Start the elimination process
    while increment <= 500000:
        if status[current_position]:  # If current position is active
            status[current_position] = False  # Mark as inactive
        
        increment += 1  # Increment the step count
        current_position = (current_position + increment) % n  # Move to the next position

    # Step 4: Check the remaining active positions
    active_positions = [pos for pos in status if pos]  # Filter for active positions
    
    # Print result based on the number of active positions
    if len(active_positions) == 0:
        print("YES")  # All positions are inactive
    else:
        print("NO")  # There are still active positions

# Example of functionality; in practice, this function would be called to execute
# elimination_process()
