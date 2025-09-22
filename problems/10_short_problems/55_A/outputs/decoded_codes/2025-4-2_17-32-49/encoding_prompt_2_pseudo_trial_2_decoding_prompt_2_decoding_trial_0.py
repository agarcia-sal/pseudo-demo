# Step 1: Get the total number of items
number_of_items = int(input())

# Step 2: Create the list to track active items
is_active = [True] * number_of_items

# Step 3: Initialize position and step count
current_position = 0
step_count = 1

# Step 4: Begin the loop with the specified condition
while step_count <= 500000:
    # Check if the current item is active
    if is_active[current_position]:
        # Mark the item as inactive
        is_active[current_position] = False
    
    # Increment the step count
    step_count += 1

    # Update the current position
    current_position = (current_position + step_count) % number_of_items

# Step 5: Create the list of remaining active items
remaining_active_items = [item for item in is_active if item]

# Step 6: Check the length of the remaining active items
if len(remaining_active_items) == 0:
    print("YES")
else:
    print("NO")
