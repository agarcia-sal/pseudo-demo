def main():
    # Read an integer input for the size of the list
    number_of_elements = int(input())

    # Initialize a list to track active status for each position
    is_active = [True] * number_of_elements

    # Initialize position and step variables
    index = 0
    step = 1

    # Loop until the step variable exceeds 500,000
    while step <= 500000:
        # Check if the current position is Active
        if is_active[index]:
            # Mark the current position as inactive
            is_active[index] = False
        
        # Increment the step variable
        step += 1
        
        # Update the index based on the step, wrapping around using modulo
        index = (index + step) % number_of_elements

    # Filter to create a list of active positions (where value is True)
    active_positions = [i for i, active in enumerate(is_active) if active]

    # Check if there are any active positions left
    if len(active_positions) == 0:
        print('YES')  # All positions are inactive
    else:
        print('NO')   # There are still active (True) positions

# Call the main function
if __name__ == "__main__":
    main()
