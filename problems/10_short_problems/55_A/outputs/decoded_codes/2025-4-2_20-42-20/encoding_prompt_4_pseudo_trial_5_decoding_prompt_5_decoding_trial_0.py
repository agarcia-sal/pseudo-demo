# Function to determine if any positions remain active after processing
def check_active_positions():
    # Get user input as an integer
    n = int(input())
    
    # Initialize a list of boolean values to True for the range 0 to n
    is_active = [True] * n
    
    # Initialize indices
    j = 0  # Current index
    i = 1  # Step increment
    
    # Loop until i exceeds 500,000
    while i <= 500000:
        # If the current position is active
        if is_active[j]:
            # Deactivate current position
            is_active[j] = False
        
        # Increment step by 1
        i += 1
        
        # Update index j in circular manner
        j = (j + i) % n
    
    # Create a list of active positions
    active_positions = [index for index, value in enumerate(is_active) if value]
    
    # Check if there are any active positions
    if len(active_positions) == 0:
        # If no active positions remain
        print('YES')
    else:
        # If there are still active positions
        print('NO')

# Call the function to execute
check_active_positions()
