def mark_positions():
    # Step 1: Get input for the number of positions
    n = int(input())
    
    # Step 2: Initialize the list of positions (all unmarked)
    positions = [True] * n

    # Step 3: Initialize counter variables
    count = 1
    current_index = 0
    
    # Step 4: Mark positions in a loop until count exceeds 500,000
    while count <= 500000:
        if positions[current_index]:  # If position is unmarked
            positions[current_index] = False  # Mark it
        
        count += 1  # Increment count
        current_index = (current_index + count) % n  # Update index with wrapping
    
    # Step 5: Check for unmarked positions
    unmarked_positions = [pos for pos in positions if pos]

    # Step 6: Produce output based on unmarked positions
    if len(unmarked_positions) == 0:
        print("YES")  # All positions are marked
    else:
        print("NO")  # Some positions remain unmarked

# Call the function to execute the program
mark_positions()
