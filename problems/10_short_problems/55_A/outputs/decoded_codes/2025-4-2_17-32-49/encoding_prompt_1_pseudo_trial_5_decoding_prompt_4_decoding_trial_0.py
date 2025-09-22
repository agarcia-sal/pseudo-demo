def main():
    # Step 2: Input a number `n` (the maximum size of the list).
    n = int(input())
    
    # Step 3: Create a list `isAvailable` of size `n` and set all elements to `True`.
    is_available = [True] * n
    
    # Step 4: Initialize two variables.
    current_position = 0  # This will track the index in `isAvailable`
    increment_value = 1    # This will be used to determine the current step size
    
    # Step 5: Set a loop to run while `increment_value` is less than or equal to 500,000.
    while increment_value <= 500000:
        # Step 5a: Check if the current position is available.
        if is_available[current_position]:
            # Step 5b: Mark this position as unavailable.
            is_available[current_position] = False
        
        # Step 5c: Increment the value and update the current position.
        increment_value += 1
        current_position = (current_position + increment_value) % n
    
    # Step 6: Create a new list of available positions.
    available_positions = [i for i in range(n) if is_available[i]]
    
    # Step 7: Check the length of available positions and output the result.
    if len(available_positions) == 0:
        print("YES")  # All positions made unavailable
    else:
        print("NO")   # There are still available positions

# Step 1: Start the program by calling the main function.
if __name__ == "__main__":
    main()
