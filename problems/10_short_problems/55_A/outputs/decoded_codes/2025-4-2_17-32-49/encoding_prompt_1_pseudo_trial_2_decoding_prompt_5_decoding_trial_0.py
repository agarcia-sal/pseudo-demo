# Function to find available positions after processing
def find_available_positions():
    # Read an integer value n from user input
    n = int(input())

    # Initialize a list to track available positions
    is_present = [True] * n  # Set all positions to True initially
    index = 0  # Current position in the list
    step = 1  # Initial step size to dictate movement

    # Processing loop, continues while step is less than or equal to 500,000
    while step <= 500000:
        # Check if the current position is available
        if is_present[index]:
            is_present[index] = False  # Mark this position as not available
        # Increment the step size
        step += 1
        # Update the index to the next position
        index = (index + step) % n  # Wrap around using modulus

    # Create a list of available positions
    available_positions = [position for position in is_present if position]

    # Check the results and print the appropriate message
    if len(available_positions) == 0:
        print("YES")  # All positions have been marked as not available
    else:
        print("NO")  # There are still available positions

# You can test the function by calling it:
# find_available_positions()
