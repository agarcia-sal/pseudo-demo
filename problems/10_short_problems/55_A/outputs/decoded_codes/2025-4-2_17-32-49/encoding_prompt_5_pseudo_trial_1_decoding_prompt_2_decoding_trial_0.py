# Start the program.

# Get Input
n = int(input())  # Read an integer value n

# Initialize List of Positions
positions = [True] * n  # Create a list of n entries, all set to True

# Set Initial Counter Variables
count = 1  # This will be our step increment
current_index = 0  # This will point to the current position in the list

# Mark Positions in a Loop
while count <= 500000:  # Repeat while count is less than or equal to 500,000
    if positions[current_index]:  # If the position at current_index is still True
        positions[current_index] = False  # Mark it as False (indicating it is marked)
    
    count += 1  # Increment count by 1
    current_index = (current_index + count) % n  # Update current_index with wrap around using modulo

# Check for Unmarked Positions
unmarked_positions = [pos for pos in positions if pos]  # Create a list of unmarked positions

# Produce Output
if len(unmarked_positions) == 0:  # If there are no unmarked positions
    print("YES")  # All positions have been marked
else:
    print("NO")  # There are still unmarked positions

# End the program.
