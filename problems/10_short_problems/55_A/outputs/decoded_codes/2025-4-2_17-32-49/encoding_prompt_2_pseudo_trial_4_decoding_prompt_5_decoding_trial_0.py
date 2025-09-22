# Define a function to check available positions based on the algorithm
def check_available_positions():
    # Read an integer value n, which represents the number of elements
    n = int(input())
    
    # Initialize a list to keep track of available positions, all set to True
    is_available = [True] * n
    # Initialize position and step variables
    position = 0 
    step = 1 
    
    # Loop until step exceeds 500,000
    while step <= 500000:
        # If current position is available, mark it as unavailable
        if is_available[position]:
            is_available[position] = False
        # Increment step
        step += 1
        # Update position to wrap around the list
        position = (position + step) % n

    # Check for available positions
    available_positions = [i for i in is_available if i]

    # Output result based on available positions
    if len(available_positions) == 0:
        print("YES")  # All positions are marked unavailable
    else:
        print("NO")   # Some positions are still available

# Call the function to test it
check_available_positions()
