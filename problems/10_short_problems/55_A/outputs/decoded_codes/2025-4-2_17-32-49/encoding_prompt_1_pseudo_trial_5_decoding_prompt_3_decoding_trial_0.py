def main():
    # Step 2: Input the maximum size of the list
    n = int(input())
    
    # Step 3: Create a list to track available positions, initialized to True
    is_available = [True] * n
    
    # Step 4: Initialize position and increment value
    current_position = 0
    increment_value = 1
    
    # Step 5: Loop until increment_value reaches 500,000
    while increment_value <= 500000:
        # If the current position is available
        if is_available[current_position]:
            # Mark the current position as unavailable
            is_available[current_position] = False
        
        # Increment to the next step
        increment_value += 1
        # Update current position with wrapping
        current_position = (current_position + increment_value) % n
    
    # Step 6: Determine available positions
    available_positions = [index for index, available in enumerate(is_available) if available]
    
    # Step 7: Check the length of available positions
    if len(available_positions) == 0:
        # All positions are unavailable
        print("YES")
    else:
        # There are still available positions
        print("NO")

if __name__ == "__main__":
    main()
