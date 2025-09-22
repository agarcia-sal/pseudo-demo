def main():
    # Step 1: Input
    n = int(input())

    # Step 2: Initialize
    is_available = [True] * n  # Create a list of size n with all positions set to True
    current_position = 0        # Initialize the current position
    increment = 1               # Starting increment

    # Step 3: Processing Loop
    while increment <= 500000:
        if is_available[current_position]:  # Check availability at the current position
            is_available[current_position] = False  # Mark this position as unavailable

        increment += 1  # Increase the increment for the next step
        current_position = (current_position + increment) % n  # Move to the next position in a circular manner

    # Step 4: Identify Unavailable Positions
    available_positions = [position for position in is_available if position]

    # Step 5: Output
    if len(available_positions) == 0:
        print("YES")  # No positions are available
    else:
        print("NO")   # Some positions are still available

# If this script is run directly, execute the main function
if __name__ == "__main__":
    main()
