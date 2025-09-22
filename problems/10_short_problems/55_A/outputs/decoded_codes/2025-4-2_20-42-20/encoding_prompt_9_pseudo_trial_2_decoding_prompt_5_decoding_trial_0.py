# Start of Program

# Receive Input:
total_positions = int(input())  # Read a number to determine the size of the list.

# Initialize List:
positions = [True] * total_positions  # Create a list with all entries set to True (unmarked).

# Set Initial Indices:
current_index = 0
step = 1

# Iterate through Marking Process:
while step <= 500000:
    if positions[current_index] == True:  # Check if the position is unmarked.
        positions[current_index] = False  # Mark the position as False (marked).
    
    step += 1  # Increment step.
    current_index = (current_index + step) % total_positions  # Update to the next position.

# Check for Unmarked Positions:
remaining_unmarked = [pos for pos in positions if pos]  # List of unmarked positions.

# Determine Result:
if not remaining_unmarked:  # If there are no unmarked positions.
    print("YES")  # Print "YES" indicating no unmarked positions remain.
else:
    print("NO")  # Print "NO" indicating there are still unmarked positions.

# End of Program
