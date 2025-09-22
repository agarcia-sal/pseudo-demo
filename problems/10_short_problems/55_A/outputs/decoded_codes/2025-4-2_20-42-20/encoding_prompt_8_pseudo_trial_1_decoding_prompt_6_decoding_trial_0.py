# Step 1: Read Input
n = int(input())  # Get an integer value representing the size of the list

# Step 2: Initialize List
is_active = [True] * n  # Create a list of size n filled with True

# Step 3: Set Counters
current_position = 0  # Initialize the current position
step_count = 1  # Initialize the step count

# Step 4: Loop Until Condition Met
while step_count <= 500000:  # Continue looping until step_count exceeds 500,000
    if is_active[current_position]:  # Check if the current position is active
        is_active[current_position] = False  # Mark this position as inactive
    
    step_count += 1  # Increment the step count
    current_position = (current_position + step_count) % n  # Update the current position using modulo

# Step 5: Check Active Positions
inactive_positions = [pos for pos in is_active if pos]  # Create a list of positions that are still True

# Step 6: Output Result
if not inactive_positions:  # If there are no active positions left
    print("YES")  # All positions have been marked inactive
else:
    print("NO")  # At least one position remains active
