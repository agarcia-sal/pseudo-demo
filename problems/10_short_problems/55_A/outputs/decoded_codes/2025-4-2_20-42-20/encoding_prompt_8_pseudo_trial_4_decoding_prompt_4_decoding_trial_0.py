def main():
    # Step 1: Get input
    n = int(input())  # Read a number n representing the size of a list

    # Step 2: Initialize a boolean list
    positions = [True] * n  # Create a list of size n, all initialized to True

    # Step 3: Set initial variables
    current_index = 0  # Track the current position being processed
    step = 1  # Determine the movement step

    # Step 4: Loop through positions
    while step <= 500000:
        if positions[current_index]:  # Check if the current position is marked
            positions[current_index] = False  # Mark the position as False

        step += 1  # Increment the step
        # Update current_index to the next position using modulo for wrap-around
        current_index = (current_index + step) % n 

    # Step 5: Check for unmarked positions
    unmarked_positions = [pos for pos in positions if pos]  # Collect all True values

    # Step 6: Output the result
    if len(unmarked_positions) == 0:  # If all positions are marked
        print('YES')
    else:
        print('NO')

# Entry point for the program
if __name__ == "__main__":
    main()
