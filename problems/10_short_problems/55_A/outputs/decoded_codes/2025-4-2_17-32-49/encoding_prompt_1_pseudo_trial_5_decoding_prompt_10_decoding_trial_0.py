def main():
    # Step 2: Input a number n (the maximum size of the list).
    n = int(input())
    
    # Step 3: Create a list isAvailable of size n and set all elements to True.
    is_available = [True] * n
    
    # Step 4: Initialize variables
    current_position = 0  # To track the index in is_available
    increment_value = 1    # To determine the current step size

    # Step 5: Loop runs while increment_value is less than or equal to 500,000
    while increment_value <= 500000:
        # If the element at is_available[current_position] is True
        if is_available[current_position]:
            # Mark current position as unavailable
            is_available[current_position] = False
        
        # Increment increment_value by 1
        increment_value += 1
        
        # Update current_position based on increment_value
        current_position = (current_position + increment_value) % n
    
    # Step 6: Create a new list availablePositions
    available_positions = [index for index, available in enumerate(is_available) if available]
    
    # Step 7: Check the length of availablePositions
    if len(available_positions) == 0:
        # Output "YES" if all positions are made unavailable
        print("YES")
    else:
        # Output "NO" if there are still available positions
        print("NO")

# Step 1: Start the program and call the main function
if __name__ == "__main__":
    main()
