# Function to determine if all positions in the list are inactive
def check_flags():
    # Step 1: Get the input for the size of the list
    n = int(input())
    
    # Step 2: Initialize the list with all elements set to True
    flag_list = [True] * n
    
    # Step 3: Set the initial values for current index and step
    current_index = 0
    step = 1
    
    # Step 4: Loop while step is less than or equal to 500,000
    while step <= 500000:
        # Check current state, if True, set to False
        if flag_list[current_index]:
            flag_list[current_index] = False  # Mark the current position as inactive
        
        # Increment step
        step += 1
        
        # Update current index with the new position (wrapping around the list)
        current_index = (current_index + step) % n
    
    # Step 5: Create a list of active positions still marked True
    active_positions = [pos for pos in flag_list if pos]
    
    # Step 6: Output the result based on the active positions
    if len(active_positions) == 0:
        print("YES")  # All positions are inactive
    else:
        print("NO")   # There are still active positions

# Call the function to execute
check_flags()
