def mark_positions():
    # Step 2: Get Input
    n = int(input())  # Read number of positions from the user

    # Step 3: Initialize List of Positions
    positions = [True] * n  # Start with all positions marked unmarked (True)

    # Step 4: Set Initial Counter Variables
    count = 1  # This will be our step increment
    current_index = 0  # This will point to the current position in the list

    # Step 5: Mark Positions in a Loop
    while count <= 500000:
        if positions[current_index]:  # If the current position is still True (unmarked)
            positions[current_index] = False  # Mark it as False (marked)

        count += 1  # Increment the count
        
        # Update current_index using the counting pattern with modulo to wrap around
        current_index = (current_index + count) % n

    # Step 6: Check for Unmarked Positions
    unmarked_positions = [position for position in positions if position]  # Extract unmarked positions

    # Step 7: Produce Output
    if len(unmarked_positions) == 0:  # If no positions are unmarked
        print("YES")  # All positions have been marked
    else:
        print("NO")  # There are still unmarked positions

# Step 1: Start the program
mark_positions()
