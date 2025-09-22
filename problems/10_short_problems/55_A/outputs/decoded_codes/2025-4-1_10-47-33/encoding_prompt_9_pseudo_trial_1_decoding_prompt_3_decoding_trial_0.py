def check_unmarked_positions():
    # Step 1: Input the total number of positions
    total_positions = int(input())
    
    # Step 2: Initialize a list to track marked positions
    marked_positions = [True] * total_positions  # All positions are initially unmarked
    
    # Step 3: Set initial index values
    current_index = 0
    step = 1
    
    # Step 4: Mark positions in a loop
    while step <= 500000:
        if marked_positions[current_index]:  # If the position is unmarked
            marked_positions[current_index] = False  # Mark it
            
        step += 1  # Increment step
        current_index = (current_index + step) % total_positions  # Loop back if necessary

    # Step 5: Check for unmarked positions
    unmarked_positions = [pos for pos in marked_positions if pos]
    
    # Step 6: Output results
    if not unmarked_positions:  # If there are no unmarked positions
        print("YES")
    else:
        print("NO")

# Example of running the function
check_unmarked_positions()
