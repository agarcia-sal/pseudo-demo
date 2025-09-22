def mark_positions():
    # Step 2: Get Input
    n = int(input())
    
    # Step 3: Initialize List
    marked = [True] * n  # All positions are initially unmarked

    # Step 4: Set Initial Variables
    current_index = 0  # Track the current position
    step = 1           # Step size for marking

    # Step 5: Mark Unmarked Positions
    while step <= 500_000:
        if marked[current_index]:  # Check if the current position is unmarked
            marked[current_index] = False  # Mark it as now marked

        step += 1  # Prepare for the next round of marking
        current_index = (current_index + step) % n  # Move to the new position circularly

    # Step 6: Check for Unmarked Positions
    unmarked_positions = [pos for pos in marked if pos]  # Get all unmarked positions

    # Step 7: Determine Output
    if not unmarked_positions:  # If there are no unmarked positions
        print("YES")
    else:
        print("NO")

# To run the function
mark_positions()
