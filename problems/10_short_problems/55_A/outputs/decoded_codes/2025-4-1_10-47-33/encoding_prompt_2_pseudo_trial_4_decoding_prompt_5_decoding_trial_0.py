def check_availability():
    # Read the size of the array from user input
    n = int(input())
    
    # Initialize the availability list with all positions set to True
    is_available = [True] * n
    current_position = 0  # Starting index
    increment = 1  # Initial step size

    # Loop until increment reaches 500,000
    while increment <= 500000:
        # Check if the current position is available
        if is_available[current_position]:
            is_available[current_position] = False  # Mark position as unavailable
        # Increase increment for the next step
        increment += 1
        # Update current position and wrap around using modulus
        current_position = (current_position + increment) % n

    # Collect all available positions
    available_positions = [pos for pos in is_available if pos]
    
    # Check the length of available positions and print the result
    if len(available_positions) == 0:
        print("YES")  # No available positions
    else:
        print("NO")  # Some positions are still available

# Testing the function (consider adding test cases as comments)
# Example inputs to test could be: 3, 10, or large numbers for performance tests
