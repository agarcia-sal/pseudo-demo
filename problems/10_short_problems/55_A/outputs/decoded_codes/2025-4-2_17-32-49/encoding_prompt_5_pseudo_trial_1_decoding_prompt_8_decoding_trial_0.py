# Start the program.

# Get Input:
n = int(input())

# Initialize List of Positions:
positions = [True] * n  # All positions are initially unmarked (True).

# Set Initial Counter Variables:
count = 1
current_index = 0

# Mark Positions in a Loop:
while count <= 500000:
    if positions[current_index]:  # Check if current position is unmarked.
        positions[current_index] = False  # Mark the position as False.

    count += 1  # Increment the count.
    current_index = (current_index + count) % n  # Update the index with wrap-around.

# Check for Unmarked Positions:
unmarked_positions = [pos for pos in positions if pos]  # Positions that are still True.

# Produce Output:
if len(unmarked_positions) == 0:  # All positions are marked.
    print("YES")
else:  # There are still unmarked positions.
    print("NO")

# End the program.
