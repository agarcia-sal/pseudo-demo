# Function to determine if all positions in a circular list are marked
def check_marked_positions():
    # Get the number of positions in the list
    n = int(input())
    
    # Initialize the marking list, all positions are initially unmarked (True)
    marked = [True] * n
    
    # Set the initial position and step
    current_index = 0
    step = 1
    
    # Mark positions in the list according to the step size
    while step <= 500000:
        # If the current position is unmarked
        if marked[current_index]:
            # Mark the current position
            marked[current_index] = False
        
        # Increment the step
        step += 1
        
        # Update the current index (wrap around using modulo)
        current_index = (current_index + step) % n
    
    # Collect positions that remain unmarked
    unmarked_positions = [pos for pos in marked if pos]
    
    # Determine and print the result based on unmarked positions
    if not unmarked_positions:
        print("YES")  # All positions were marked
    else:
        print("NO")   # There are still unmarked positions

# Call the function to execute
check_marked_positions()
