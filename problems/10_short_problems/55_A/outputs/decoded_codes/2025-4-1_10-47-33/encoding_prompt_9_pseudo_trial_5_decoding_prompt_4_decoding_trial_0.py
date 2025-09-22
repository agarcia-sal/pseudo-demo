def mark_positions():
    # Step 1: Initialize Variables
    number_of_positions = int(input())
    marked_positions = [True] * number_of_positions  # List initialized to True
    current_index = 0
    step_count = 1

    # Step 2: Perform Marking Process
    while step_count <= 500000:
        if marked_positions[current_index]:  # Check if the current position is marked
            marked_positions[current_index] = False  # Mark this position as False
        step_count += 1  # Increment the step count
        current_index = (current_index + step_count) % number_of_positions  # Update the index

    # Step 3: Check for Unmarked Positions
    unmarked_positions = [pos for pos in marked_positions if pos]  # Filter True values
    if not unmarked_positions:  # If there are no unmarked positions left
        print("YES")  # All positions are marked
    else:
        print("NO")  # There are unmarked positions remaining

# Run the function to execute
mark_positions()
