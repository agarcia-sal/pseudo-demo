# Step 1: Initialize the Variables
n = int(input())  # Read an integer value representing the size of the list
status = [True] * n  # Create a list called "status" with True values
current_position = 0  # Initialize current_position to 0
increment = 1  # Initialize increment to 1

# Step 2: Start the Elimination Process
while increment <= 500000:  # Continue until increment exceeds 500,000
    if status[current_position]:  # Check if the status at current_position is True
        status[current_position] = False  # Mark the position as inactive
    increment += 1  # Increment the increment counter by 1
    current_position = (current_position + increment) % n  # Update current_position with wrap-around

# Step 3: Check the Remaining Active Positions
active_positions = [pos for pos in status if pos]  # Create a list of active positions (True values)
if len(active_positions) == 0:  # Check if there are no active positions left
    print("YES")  # Output "YES" if all positions are inactive
else:
    print("NO")  # Output "NO" if there are still active positions
