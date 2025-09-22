def main():
    # Initialize Variables
    number_of_positions = int(input())
    marked_positions = [True] * number_of_positions  # All positions are initially marked
    current_index = 0
    step_count = 1

    # Perform Marking Process
    while step_count <= 500000:
        if marked_positions[current_index]:  # Check if the current position is marked
            marked_positions[current_index] = False  # Mark this position as False
        
        step_count += 1  # Increment the step count
        current_index = (current_index + step_count) % number_of_positions  # Update position

    # Check for Unmarked Positions
    unmarked_positions = [pos for pos in marked_positions if pos]  # List of unmarked positions
    if not unmarked_positions:  # If there are no True values remaining
        print("YES")  # All positions were marked
    else:
        print("NO")  # There are still unmarked positions

# Entry point of the program
if __name__ == "__main__":
    main()
