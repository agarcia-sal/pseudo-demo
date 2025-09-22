# Initialize the Variables
n = int(input())
status = [True] * n  # Create a list with n True values
current_position = 0
increment = 1

# Start the Elimination Process
while increment <= 500000:
    if status[current_position]:
        status[current_position] = False  # Mark position as inactive
    increment += 1
    current_position = (current_position + increment) % n  # Move to the next position

# Check the Remaining Active Positions
active_positions = [pos for pos in status if pos]  # Create a list of active positions
if len(active_positions) == 0:
    print("YES")  # All positions are inactive
else:
    print("NO")   # There are still active positions
