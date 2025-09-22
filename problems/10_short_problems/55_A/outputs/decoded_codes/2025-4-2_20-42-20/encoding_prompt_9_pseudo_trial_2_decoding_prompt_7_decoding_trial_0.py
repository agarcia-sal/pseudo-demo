# Start of Program

# Step 2: Receive Input
total_positions = int(input())  # Read the total number of positions

# Step 3: Initialize List
positions = [True] * total_positions  # Create a list with all entries set to True (unmarked)

# Step 4: Set Initial Indices
current_index = 0  # Start from the first position
step = 1  # Initial step size

# Step 5: Iterate through Marking Process
while step <= 500000:  # Continue until step exceeds 500,000
    if positions[current_index]:  # Check if the current position is unmarked
        positions[current_index] = False  # Mark the current position as False (marked)
        
    step += 1  # Increment the step size
    current_index = (current_index + step) % total_positions  # Update the current index

# Step 6: Check for Unmarked Positions
remaining_unmarked = [pos for pos in positions if pos]  # List of unmarked positions

# Step 7: Determine Result
if not remaining_unmarked:  # If there are no unmarked positions
    print("YES")  # Print "YES" if all positions are marked
else:
    print("NO")  # Print "NO" if there are unmarked positions

# End of Program
