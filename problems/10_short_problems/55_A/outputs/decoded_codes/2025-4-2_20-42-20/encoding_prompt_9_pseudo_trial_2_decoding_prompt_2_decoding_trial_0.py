# Start of Program

# Receive Input
total_positions = int(input())

# Initialize List
positions = [True] * total_positions  # Create list of True values

# Set Initial Indices
current_index = 0
step = 1

# Iterate through Marking Process
while step <= 500000:
    if positions[current_index]:  # If the position is unmarked
        positions[current_index] = False  # Mark the position as False (marked)
    
    step += 1  # Increment the step
    current_index = (current_index + step) % total_positions  # Calculate next position

# Check for Unmarked Positions
remaining_unmarked = [pos for pos in positions if pos]  # Get all unmarked positions

# Determine Result
if not remaining_unmarked:  # If there are no unmarked positions
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"

# End of Program
