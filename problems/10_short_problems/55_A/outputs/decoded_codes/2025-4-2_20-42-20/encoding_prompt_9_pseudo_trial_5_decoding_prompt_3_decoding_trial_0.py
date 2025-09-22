def mark_positions():
    # Step 2: Receive input
    size = int(input())
    
    # Step 3: Initialize list
    positions = [True] * size  # List with all elements set to True
    
    # Step 4: Set counters
    current_increment = 1
    current_position_index = 0
    
    # Step 5: Mark positions
    while current_increment <= 500000:
        if positions[current_position_index]:
            positions[current_position_index] = False  # Mark position as False
        
        current_increment += 1
        # Update current_position_index with wrap-around using modulo
        current_position_index = (current_position_index + current_increment) % size
    
    # Step 6: Check status of positions
    unmarked_positions = [pos for pos in positions if pos]  # Liste of True values
    
    # Step 7: Output result
    if len(unmarked_positions) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
mark_positions()
