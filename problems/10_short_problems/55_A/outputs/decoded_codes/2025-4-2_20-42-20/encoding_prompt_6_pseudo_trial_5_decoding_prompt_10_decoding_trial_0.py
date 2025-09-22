def elimination_game(n):
    # Step 1: Initialize the 'isAlive' array with True values
    is_alive = [True] * n
    current_index = 0
    step_count = 1

    # Step 2: Execute the elimination process
    while step_count <= 500000:
        if is_alive[current_index]:  # If the current position is alive
            is_alive[current_index] = False  # Mark as eliminated
        step_count += 1  # Increment the step count
        current_index = (current_index + step_count) % n  # Update the index with wrap around

    # Step 3: Create a list of remaining alive positions
    remaining = [alive for alive in is_alive if alive]

    # Check if there are any remaining alive positions
    if len(remaining) == 0:
        print("YES")  # Output if no one is alive
    else:
        print("NO")   # Output if there are still persons alive


# Input: Reading size of the array
n = int(input())
elimination_game(n)
