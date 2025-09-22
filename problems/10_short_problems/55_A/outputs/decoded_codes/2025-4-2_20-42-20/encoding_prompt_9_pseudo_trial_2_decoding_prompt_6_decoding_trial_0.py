# Start of Program

# Step 2: Receive Input
total_positions = int(input())  # Read a number to determine the size of the list

# Step 3: Initialize List
positions = [True] * total_positions  # List with `total_positions` entries set to True

# Step 4: Set Initial Indices
current_index = 0  # Initialize the current index to 0
step = 1  # Initialize step to 1

# Step 5: Iterate through Marking Process
while step <= 500000:  # Continue marking while step is less than or equal to 500,000
    if positions[current_index]:  # Check if the current position is unmarked
        positions[current_index] = False  # Mark the current position as False (marked)
    
    step += 1  # Increment step by 1
    current_index = (current_index + step) % total_positions  # Update current_index using the formula

# Step 6: Check for Unmarked Positions
remaining_unmarked = [pos for pos in positions if pos]  # List of all unmarked positions (True values)

# Step 7: Determine Result
if not remaining_unmarked:  # If there are no unmarked positions left
    print("YES")  # Print "YES" indicating no unmarked positions remain
else:
    print("NO")  # Print "NO" indicating there are still unmarked positions

# End of Program
