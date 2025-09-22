# Step 1: Get the total number of items from user input
number_of_items = int(input())

# Step 2: Create a list that tracks active items, initialized to True
is_active = [True] * number_of_items

# Step 3: Initialize current position and step count
current_position = 0
step_count = 1

# Step 4: Loop until step_count exceeds 500,000
while step_count <= 500000:
    # Check if the current item is still active
    if is_active[current_position]:
        # Mark the item as inactive
        is_active[current_position] = False
    
    # Increment the step_count
    step_count += 1
    
    # Update the current_position with wrapping
    current_position = (current_position + step_count) % number_of_items

# Step 5: Create a list of remaining active items
remaining_active_items = [item for item in is_active if item]

# Step 6: Check the length of remaining_active_items
if len(remaining_active_items) == 0:
    print("YES")  # Output if no items are active
else:
    print("NO")   # Output if there are still active items
