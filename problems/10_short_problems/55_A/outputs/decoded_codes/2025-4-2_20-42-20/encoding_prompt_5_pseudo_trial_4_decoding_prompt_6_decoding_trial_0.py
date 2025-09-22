# Step 1: Read the integer value representing the size of the list (n)
n = int(input())

# Step 2: Initialize the list "status" with n True values
status = [True] * n

# Step 3: Initialize counter variables
current_position = 0
increment = 1

# Step 4: Start the elimination process
while increment <= 500000:
    # Check if the status at current_position is True
    if status[current_position]:
        # Mark the current position as inactive (False)
        status[current_position] = False
        
    # Increment the increment counter
    increment += 1
    
    # Move to the next position
    current_position = (current_position + increment) % n

# Step 5: Create a list of active positions that are still True
active_positions = [pos for pos in status if pos]

# Step 6: Check if there are any active positions left
if len(active_positions) == 0:
    print("YES")  # All positions are inactive
else:
    print("NO")   # There are still active positions
