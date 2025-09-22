# Start of the code

# Step 1: Input the number of positions (n)
number_of_positions = int(input())

# Step 2: Initialize a list to track active positions, set to True initially
active_positions = [True] * number_of_positions

# Step 3: Initialize counters
index = 0
increment = 1

# Step 4: Loop through up to 500,000 iterations
while increment <= 500000:
    # If the current position is active
    if active_positions[index]:
        # Mark the current position as inactive
        active_positions[index] = False

    # Increase increment for the next step
    increment += 1

    # Move to the next position, wrap around using modulo
    index = (index + increment) % number_of_positions

# Step 5: Filter the list to find all active positions remaining
remaining_active_positions = [pos for pos in active_positions if pos]

# Step 6: Output result
if len(remaining_active_positions) == 0:
    print('YES')  # All positions are inactive
else:
    print('NO')   # Some positions are still active

# End of the code
