# Begin Program

# Step 2: Get Input
n = int(input())  # Read a number representing the number of positions

# Step 3: Initialize List
marked_positions = [True] * n  # Create a list of size n filled with True (unmarked)

# Step 4: Set Initial Variables
current_index = 0  # This will track the current position
step = 1  # This will determine the step size for marking

# Step 5: Mark Unmarked Positions
while step <= 500000:  # Continue while step is less than or equal to 500,000
    if marked_positions[current_index]:  # Check if the current position is unmarked
        marked_positions[current_index] = False  # Mark the current position
    step += 1  # Increase step by 1
    current_index = (current_index + step) % n  # Update current index circularly

# Step 6: Check for Unmarked Positions
unmarked_positions = [position for position in marked_positions if position]  # List of unmarked positions (True values)

# Step 7: Determine Output
if not unmarked_positions:  # If there are no unmarked positions
    print("YES")  # All positions are marked
else:
    print("NO")  # There are still unmarked positions

# End Program
