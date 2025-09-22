# Start the program
def check_availability():
    # Input a number n (the maximum size of the list)
    n = int(input())
    
    # Create a list isAvailable of size n and set all elements to True
    is_available = [True] * n
    
    # Initialize variables
    current_position = 0  # Tracks the index in isAvailable
    increment_value = 1    # Used to determine the current step size

    # Loop while increment_value is less than or equal to 500,000
    while increment_value <= 500000:
        # If isAvailable[current_position] is True
        if is_available[current_position]:
            # Mark the position as unavailable
            is_available[current_position] = False
        
        # Increment increment_value by 1
        increment_value += 1
        
        # Update current_position to wrap around
        current_position = (current_position + increment_value) % n
    
    # Create a list availablePositions with all still True elements
    available_positions = [index for index, available in enumerate(is_available) if available]
    
    # Check the length of availablePositions
    if len(available_positions) == 0:
        # Output "YES" if all positions were made unavailable
        print("YES")
    else:
        # Output "NO" if there are still available positions
        print("NO")

# Uncomment the line below to run the program
# check_availability()
