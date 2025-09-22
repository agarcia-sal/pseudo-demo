# Start the program.

# Get Input:
n = int(input())  # Read an integer value `n` from the user.

# Initialize List of Positions:
positions = [True] * n  # Create a list called `positions` with `n` entries, all initially True.

# Set Initial Counter Variables:
count = 1  # Set `count` to 1.
current_index = 0  # Set `current_index` to 0.

# Mark Positions in a Loop:
while count <= 500000:  # Repeat while `count` is less than or equal to 500,000.
    if positions[current_index]:  # If the position at `current_index` is still marked as True:
        positions[current_index] = False  # Mark it as False.

    count += 1  # Increment `count` by 1.
    current_index = (current_index + count) % n  # Update `current_index`.

# Check for Unmarked Positions:
unmarked_positions = [pos for pos in positions if pos]  # Create a list of unmarked positions.

# Produce Output:
if len(unmarked_positions) == 0:  # If there are no unmarked positions:
    print("YES")  # Print "YES".
else:
    print("NO")  # Otherwise, print "NO".

# End the program.
