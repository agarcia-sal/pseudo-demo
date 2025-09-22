def elimination_game():
    # Read the size of the array
    n = int(input())
    
    # Initialize an array to represent if each person is alive
    is_alive = [True] * n
    current_index = 0
    step_count = 1

    # Run the elimination process
    while step_count <= 500000:
        if is_alive[current_index]:
            # Mark the current index as eliminated
            is_alive[current_index] = False
        
        # Increment the step count
        step_count += 1
        
        # Update the current index with wrap-around
        current_index = (current_index + step_count) % n

    # Create a list of remaining alive persons
    remaining = [alive for alive in is_alive if alive]

    # Check if any person is still alive
    if len(remaining) == 0:
        print("YES")  # No one is alive
    else:
        print("NO")   # There are still people alive

# Example of running the function
elimination_game()
