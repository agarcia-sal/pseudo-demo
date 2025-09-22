def main():
    # Step 1: Receive Input
    total_positions = int(input())

    # Step 2: Initialize List
    positions = [True] * total_positions  # All positions initially unmarked

    # Step 3: Set Initial Indices
    current_index = 0
    step = 1

    # Step 4: Iterate through Marking Process
    while step <= 500000:
        if positions[current_index]:  # Check if the position is unmarked
            positions[current_index] = False  # Mark the position as False (marked)

        step += 1  # Increment step
        # Update current_index using the formula
        current_index = (current_index + step) % total_positions

    # Step 5: Check for Unmarked Positions
    remaining_unmarked = [pos for pos in positions if pos]

    # Step 6: Determine Result
    if not remaining_unmarked:  # If there are no unmarked positions left
        print("YES")  # All positions are marked
    else:
        print("NO")  # There are still unmarked positions

# Call the main function to execute the program
if __name__ == "__main__":
    main()
