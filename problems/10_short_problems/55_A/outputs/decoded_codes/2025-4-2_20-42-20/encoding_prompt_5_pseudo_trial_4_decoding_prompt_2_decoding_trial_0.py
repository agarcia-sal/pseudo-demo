# Step 1: Read an integer value representing the size of the list (n).
n = int(input())

# Step 2: Create a list called "status" with "True" values.
status = [True] * n

# Step 3: Initialize counter variables.
current_position = 0
increment = 1

# Step 4: Start the elimination process.
while increment <= 500000:
    # Check if the status at "current_position" is "True".
    if status[current_position]:
        # If it is "True", set it to "False".
        status[current_position] = False
    
    # Increment "increment" by 1.
    increment += 1
    
    # Update "current_position" using the defined formula.
    current_position = (current_position + increment) % n

# Step 5: Check the remaining active positions.
active_positions = [pos for pos in status if pos]

# Step 6: Determine the result based on the length of active_positions.
if len(active_positions) == 0:
    print("YES")  # All positions are inactive.
else:
    print("NO")   # There are still active positions.
