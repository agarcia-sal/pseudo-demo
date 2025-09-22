# Start of the program

# Get the number of positions (n) from the user
number_of_positions = int(input())

# Initialize a list to track active positions, all set to True initially
active_positions = [True] * number_of_positions

# Initialize counters
index = 0
increment = 1

# Loop through up to 500,000 iterations
while increment <= 500000:
    # If the current position is active
    if active_positions[index]:
        # Mark the current position as inactive
        active_positions[index] = False
        
    # Increase increment for the next step
    increment += 1
    
    # Move to the next position, wrapping around using modulo
    index = (index + increment) % number_of_positions

# Filter the list to find all active positions remaining
remaining_active_positions = [p for p in active_positions if p]

# Output result
if len(remaining_active_positions) == 0:
    print('YES')  # All positions are inactive
else:
    print('NO')   # Some positions are still active

# End of the program
