# Function to check active positions based on the algorithm described in the pseudocode
def check_active_positions():
    # Read an integer input to determine the size of the list
    number_of_elements = int(input())

    # Initialize a list to track boolean values (True/False) for each position
    is_active = [True] * number_of_elements

    # Initialize position variables for iterating
    index = 0
    step = 1

    # Loop until the step variable exceeds 500,000
    while step <= 500000:
        # Check if the current position in the list is marked as active
        if is_active[index]:
            # Mark the current position as inactive
            is_active[index] = False
        
        # Increment the step variable
        step += 1

        # Update the index based on the step, wrapping around using modulo
        index = (index + step) % number_of_elements
    
    # Filter to create a list of active positions (where value is True)
    active_positions = [pos for pos in is_active if pos]

    # Check if there are no active positions left
    if len(active_positions) == 0:
        print('YES')  # All positions are inactive
    else:
        print('NO')   # There are still active (True) positions

# Consider testing with a simple call to the function; 
# Uncomment the next line to run the code:
# check_active_positions()
