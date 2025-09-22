def deactivate_positions():
    # Step 1: Read an integer value 'n' from user input
    n = int(input())

    # Step 2: Create a boolean list 'isActive' with all elements initialized to True
    isActive = [True] * n

    # Step 3: Initialize tracking variables
    index = 0  # Current position in the list
    step = 1   # Steps to move after each iteration

    # Step 4: Iterate through steps, stopping at 500,000
    while step <= 500000:
        # Check if the current position at 'index' is active
        if isActive[index]:
            # Deactivate the position
            isActive[index] = False
        
        # Increment the step for the next iteration
        step += 1

        # Update the index with wrapping around using modulo
        index = (index + step) % n

    # Step 5: Create a list of remaining active positions
    activePositions = [pos for pos in isActive if pos]

    # Step 6: Determine the output based on active positions
    if len(activePositions) == 0:
        print("YES")  # All positions are deactivated
    else:
        print("NO")   # Some positions are still active

# Call the function to run the program
deactivate_positions()
