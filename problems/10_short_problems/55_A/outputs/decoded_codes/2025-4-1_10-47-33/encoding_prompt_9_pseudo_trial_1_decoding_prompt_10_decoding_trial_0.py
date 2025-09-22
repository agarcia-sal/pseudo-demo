def main():
    # Step 1: Input the total number of positions.
    total_positions = int(input())

    # Step 2: Initialize a list to track marked positions.
    marked_positions = [True] * total_positions  # All positions are initially unmarked

    # Step 3: Set initial index values.
    current_index = 0
    step = 1

    # Step 4: Mark positions in a loop.
    while step <= 500000:
        if marked_positions[current_index]:  # If position is unmarked
            marked_positions[current_index] = False  # Mark it
            
        step += 1
        current_index = (current_index + step) % total_positions  # Update index
        
    # Step 5: Check for unmarked positions.
    unmarked_positions = [p for p in marked_positions if p]  # Keep only unmarked (True) positions

    # Step 6: Output results.
    if not unmarked_positions:  # If all positions are marked
        print("YES")
    else:
        print("NO")


# Run the main function.
if __name__ == "__main__":
    main()
