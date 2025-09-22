# Start of Program

# Receive Input
total_positions = int(input())  # Read the number of total positions from the user

# Initialize List
positions = [True] * total_positions  # Create a list of True values representing unmarked positions

# Set Initial Indices
current_index = 0
step = 1

# Iterate through Marking Process
while step <= 500000:
    if positions[current_index]:  # If the current position is unmarked
        positions[current_index] = False  # Mark it as False (marked)
    step += 1  # Increment the step count
    current_index = (current_index + step) % total_positions  # Calculate the next position

# Check for Unmarked Positions
remaining_unmarked = [pos for pos in positions if pos]  # List of all unmarked positions (True)

# Determine Result
if not remaining_unmarked:  # If the list of unmarked positions is empty
    print("YES")  # All positions are marked
else:
    print("NO")  # Some positions remain unmarked

# End of Program
