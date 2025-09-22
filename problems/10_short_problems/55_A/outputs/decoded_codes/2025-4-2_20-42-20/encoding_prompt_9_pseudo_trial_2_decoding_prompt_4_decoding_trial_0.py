def main():
    # Step 1: Receive Input
    total_positions = int(input())
    
    # Step 2: Initialize List
    positions = [True] * total_positions  # True means unmarked positions

    # Step 3: Set Initial Indices
    current_index = 0
    step = 1

    # Step 4: Iterate through Marking Process
    while step <= 500000:
        if positions[current_index]:  # Only unmarked positions
            positions[current_index] = False  # Mark the position
            
        # Step 5: Update indices for the next step
        step += 1
        current_index = (current_index + step) % total_positions

    # Step 6: Check for Unmarked Positions
    remaining_unmarked = [pos for pos in positions if pos]

    # Step 7: Determine Result
    if not remaining_unmarked:  # If there are no unmarked positions left
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
