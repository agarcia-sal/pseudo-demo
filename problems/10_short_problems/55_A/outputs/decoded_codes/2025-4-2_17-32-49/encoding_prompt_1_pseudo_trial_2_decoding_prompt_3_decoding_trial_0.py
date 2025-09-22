def mark_positions():
    # Step 1: Input
    n = int(input())  # Read an integer value 'n' from user input.
    
    # Step 2: Initialization
    is_present = [True] * n  # Create a list to track positions available, initialized to True
    index = 0  # Track the current position in the list
    step = 1  # Initial step size

    # Step 3: Processing Loop
    while step <= 500000:
        if is_present[index]:  # Check if the current position is available
            is_present[index] = False  # Mark this position as not available
        step += 1  # Increment the step size
        index = (index + step) % n  # Update index within bounds of the list

    # Step 4: Checking Results
    available_positions = [pos for pos in is_present if pos]  # List of available positions
    if len(available_positions) == 0:  # Check if no positions are available
        print("YES")  # All positions have been marked as not available
    else:
        print("NO")  # There are still positions available

# Call the function to execute the process
mark_positions()
