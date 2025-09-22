# Define the function to track marked positions in a game
def mark_positions():
    # Step 1: Input the total number of positions
    total_positions = int(input())

    # Step 2: Initialize a list to track marked positions
    # Initially, all positions are unmarked (True)
    marked_positions = [True] * total_positions

    # Step 3: Set initial index values
    current_index = 0
    step = 1

    # Step 4: Mark positions in a loop
    while step <= 500_000:
        # Check if the current position is unmarked
        if marked_positions[current_index]:
            # Mark the position as False (marked)
            marked_positions[current_index] = False

        # Update values for the next iteration
        step += 1
        current_index = (current_index + step) % total_positions  # Wrap around the list

    # Step 5: Check for unmarked positions
    unmarked_positions = [pos for pos in marked_positions if pos]

    # Step 6: Output results
    if not unmarked_positions:
        print("YES")  # All positions are marked
    else:
        print("NO")   # There are unmarked positions

# Call the function to execute the marking process
mark_positions()
