# Purpose: Determine if there exists any unmarked position in a circular list after processing a sequence of iterations.

# Step 1: Receive Input
n = int(input())

# Step 2: Initialize List
positions = [True] * n  # All positions are initially unmarked (True)

# Step 3: Set Starting Variables
current_position = 0
step_count = 1

# Step 4: Loop Until Step Count Exceeds Limit
while step_count <= 500000:
    if positions[current_position]:  # If position is unmarked
        positions[current_position] = False  # Mark it as False (marked)
    
    step_count += 1  # Increment step count
    current_position = (current_position + step_count) % n  # Update position in a circular manner

# Step 5: Collect Remaining Unmarked Positions
unmarked_positions = [pos for pos in positions if pos]  # List of all true entries (unmarked)

# Step 6: Check for Unmarked Positions
if len(unmarked_positions) == 0:
    print('YES')  # No unmarked positions
else:
    print('NO')  # There are unmarked positions
