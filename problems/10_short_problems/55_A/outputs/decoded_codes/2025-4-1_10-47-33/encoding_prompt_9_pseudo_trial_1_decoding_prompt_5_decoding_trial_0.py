# Function to determine if there are any unmarked positions in the game
def check_unmarked_positions():
    # Input the total number of positions
    total_positions = int(input())
    
    # Initialize a list to track marked positions (True means unmarked)
    marked_positions = [True] * total_positions
    
    # Set initial index values
    current_index = 0
    step = 1
    
    # Mark positions in a loop
    while step <= 500000:
        if marked_positions[current_index]:  # If the position is unmarked
            marked_positions[current_index] = False  # Mark the position
        step += 1  # Increment the step
        current_index = (current_index + step) % total_positions  # Update index with wrapping
    
    # Check for unmarked positions
    unmarked_positions = [pos for pos in marked_positions if pos]  # Collect all unmarked positions
    
    # Output results
    if not unmarked_positions:  # If there are no unmarked positions
        print("YES")
    else:
        print("NO")

# Call the function to execute the logic
check_unmarked_positions()
