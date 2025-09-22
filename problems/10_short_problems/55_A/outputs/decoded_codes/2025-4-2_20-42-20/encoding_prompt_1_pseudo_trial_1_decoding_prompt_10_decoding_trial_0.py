def deactivate_positions():
    # Step 1: Read an integer value from user input
    n = int(input())

    # Step 2: Create a boolean list initialized to True
    is_active = [True] * n

    # Step 3: Initialize index and step
    index = 0
    step = 1

    # Step 4: Iterate through steps until step exceeds 500,000
    while step <= 500000:
        # Check if the current position is active
        if is_active[index]:
            is_active[index] = False
        
        # Increment the step
        step += 1
        
        # Update index using modulo to wrap around
        index = (index + step) % n

    # Step 5: Create a list of active positions
    active_positions = [pos for pos in is_active if pos]

    # Step 6: Determine the output
    if len(active_positions) == 0:
        print("YES")
    else:
        print("NO")

# Calling the function to run the program
deactivate_positions()
