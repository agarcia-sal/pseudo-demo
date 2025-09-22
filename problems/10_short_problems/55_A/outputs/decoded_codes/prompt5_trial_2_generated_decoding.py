# This program determines if all positions in a list are marked or not.

def check_marked_positions():
    # Step 1: Get user input for number of positions
    n = int(input())
    
    # Step 2: Initialize a list to track marked positions
    marked_positions = [True] * n
    
    # Step 3: Initialize indexing variables
    current_index = 0
    increment = 1
    
    # Step 4: Marking process
    while increment <= 500000:
        if marked_positions[current_index]:  # If current position is marked
            marked_positions[current_index] = False  # Mark it as unmarked
            
        increment += 1  # Increase the increment
        current_index = (current_index + increment) % n  # Wrap around the index
    
    # Step 5: Check for unmarked positions
    unmarked_positions = [pos for pos in marked_positions if pos]  # Collect unmarked positions
    
    # Step 6: Determine the output
    if not unmarked_positions:  # If there are no unmarked positions
        print("YES")  # All positions are marked
    else:
        print("NO")  # There are unmarked positions

# The function can be called to run the program
check_marked_positions()
