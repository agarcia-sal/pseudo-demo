def mark_positions():
    # Step 2: Receive Input
    size = int(input())
    
    # Step 3: Initialize List
    positions = [True] * size

    # Step 4: Set Counters
    current_increment = 1
    current_position_index = 0

    # Step 5: Mark Positions
    while current_increment <= 500000:
        # Check if the current position is unmarked
        if positions[current_position_index]:
            # Mark the position as False
            positions[current_position_index] = False
        
        # Increment the current_increment
        current_increment += 1
        
        # Update the current position index
        current_position_index = (current_position_index + current_increment) % size

    # Step 6: Check Status of Positions
    unmarked_positions = [pos for pos in positions if pos]

    # Step 7: Output Result
    if len(unmarked_positions) == 0:
        print("YES")
    else:
        print("NO")

# Call the function
mark_positions()
