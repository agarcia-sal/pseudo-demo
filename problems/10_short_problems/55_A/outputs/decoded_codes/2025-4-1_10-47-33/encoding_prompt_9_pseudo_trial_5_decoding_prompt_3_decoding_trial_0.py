def marking_process():
    # Step 1: Initialize Variables
    number_of_positions = int(input())
    marked_positions = [True] * number_of_positions  # List of marked positions
    current_index = 0
    step_count = 1

    # Step 2: Perform Marking Process
    while step_count <= 500000:
        if marked_positions[current_index]:  # Check if the current position is marked
            marked_positions[current_index] = False  # Mark the position as False

        step_count += 1  # Increment step count
        current_index = (current_index + step_count) % number_of_positions  # Update index with wrap-around

    # Step 3: Check for Unmarked Positions
    unmarked_positions = [pos for pos in marked_positions if pos]  # Create list of unmarked positions
    if not unmarked_positions:  # If there are no unmarked positions
        print("YES")  # All positions are marked
    else:
        print("NO")  # There are still unmarked positions

# Call the function to execute the marking process
marking_process()
