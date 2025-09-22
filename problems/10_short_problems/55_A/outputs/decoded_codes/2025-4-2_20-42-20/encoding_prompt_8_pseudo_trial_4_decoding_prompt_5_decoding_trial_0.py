# Function to determine if all positions can be marked as 'False'
def check_positions():
    # Get input for the size of the list
    n = int(input())
    
    # Initialize a boolean list with all positions set to True
    positions = [True] * n
    
    # Initialize the current index and step variables
    current_index = 0
    step = 1
    
    # Loop through positions for a maximum of 500,000 iterations
    while step <= 500000:
        # Check if the current position is marked True
        if positions[current_index]:
            # Mark the position as False
            positions[current_index] = False
        
        # Increment the step
        step += 1
        
        # Update the current index, wrapping around using modulo operation
        current_index = (current_index + step) % n
    
    # Create a list of unmarked positions (still True)
    unmarked_positions = [pos for pos in positions if pos]
    
    # Output the result based on the length of unmarked_positions
    if len(unmarked_positions) == 0:
        print('YES')
    else:
        print('NO')

# Example usage
check_positions()
