# Step 1: Get the total number of items
number_of_items = int(input())

# Step 2: Create a list to track active items
is_active = [True] * number_of_items

# Step 3: Initialize current position and step count
current_position = 0
step_count = 1

# Step 4: Begin the loop
while step_count <= 500000:
    # Check if the item at the current position is still active
    if is_active[current_position]:
        # Mark it as inactive
        is_active[current_position] = False
        
        # Increment step count
        step_count += 1
        
        # Update current position
        current_position = (current_position + step_count) % number_of_items

# Step 5: Create a list of remaining active items
remaining_active_items = [item for item in is_active if item]

# Step 6: Check the length of the remaining active items
if len(remaining_active_items) == 0:
    print("YES")
else:
    print("NO")
