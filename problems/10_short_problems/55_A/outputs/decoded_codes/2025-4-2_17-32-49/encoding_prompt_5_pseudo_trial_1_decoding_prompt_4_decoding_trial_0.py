def main():
    # Step 2: Get Input
    n = int(input())
    
    # Step 3: Initialize List of Positions
    positions = [True] * n  # All positions are initially unmarked (True)
    
    # Step 4: Set Initial Counter Variables
    count = 1
    current_index = 0

    # Step 5: Mark Positions in a Loop
    while count <= 500000:
        if positions[current_index]:  # If the position is still unmarked
            positions[current_index] = False  # Mark the position

        count += 1
        current_index = (current_index + count) % n  # Update current index with wrap-around

    # Step 6: Check for Unmarked Positions
    unmarked_positions = [pos for pos in positions if pos]

    # Step 7: Produce Output
    if len(unmarked_positions) == 0:
        print("YES")  # All positions marked
    else:
        print("NO")  # Some positions unmarked

# Execute the main function
if __name__ == "__main__":
    main()
