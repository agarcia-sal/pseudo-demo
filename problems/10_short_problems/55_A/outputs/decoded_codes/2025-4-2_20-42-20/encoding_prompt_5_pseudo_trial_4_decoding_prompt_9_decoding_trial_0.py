# Read integer input for the size of the list
n = int(input())

# Initialize the list with True values indicating all positions are active
status = [True] * n

# Initialize counter variables
current_position = 0
increment = 1

# Start the elimination process
while increment <= 500000:
    # Check if the current position is active
    if status[current_position]:
        # Mark the current position as inactive
        status[current_position] = False
        
    # Increment the counter
    increment += 1
    
    # Move to the next position using the formula
    current_position = (current_position + increment) % n

# Create a list of active positions remaining in the status
active_positions = [i for i in status if i]

# Check if there are any active positions left
if len(active_positions) == 0:
    print("YES")  # Successful elimination, all positions are inactive
else:
    print("NO")   # There are still active positions
