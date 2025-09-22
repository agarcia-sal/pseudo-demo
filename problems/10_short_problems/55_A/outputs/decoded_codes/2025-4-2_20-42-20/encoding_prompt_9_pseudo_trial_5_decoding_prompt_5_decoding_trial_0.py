# Define a function to determine if all positions can be marked as false
def mark_positions():
    # Step 2: Receive input for the number of positions
    size = int(input())
    
    # Step 3: Initialize the list of positions, all set to True
    positions = [True] * size
    
    # Step 4: Set counters
    current_increment = 1
    current_position_index = 0

    # Step 5: Mark positions while current_increment is within bounds
    while current_increment <= 500000:
        if positions[current_position_index]:  # If position is unmarked
            positions[current_position_index] = False  # Mark it as false
        
        # Increment current_increment
        current_increment += 1
        
        # Update current_position_index with modulo operation
        current_position_index = (current_position_index + current_increment) % size
    
    # Step 6: Check status of positions
    unmarked_positions = [pos for pos in positions if pos]  # Create a list of unmarked positions (True values)

    # Step 7: Output result
    if len(unmarked_positions) == 0:
        print("YES")  # All positions marked
    else:
        print("NO")   # Some positions remain unmarked

# Call the function to execute the logic
mark_positions()
