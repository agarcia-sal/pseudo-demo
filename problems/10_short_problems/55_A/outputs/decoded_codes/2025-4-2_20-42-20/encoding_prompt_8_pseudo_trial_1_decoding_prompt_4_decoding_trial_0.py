def main():
    # Step 1: Read Input
    n = int(input())
    
    # Step 2: Initialize List
    is_active = [True] * n
    
    # Step 3: Set Counters
    current_position = 0
    step_count = 1
    
    # Step 4: Loop Until Condition Met
    while step_count <= 500000:
        if is_active[current_position]:
            is_active[current_position] = False  # Mark this position as inactive
        
        # Increment step count and update current position
        step_count += 1
        current_position = (current_position + step_count) % n  # Wrap around with mod

    # Step 5: Check Active Positions
    inactive_positions = [pos for pos in is_active if pos]  # List of still active positions

    # Step 6: Output Result
    if not inactive_positions:  # If inactive_positions is empty
        print("YES")  # All positions are inactive
    else:
        print("NO")   # At least one position remains active

# Call the main function to execute
if __name__ == "__main__":
    main()
