# Step 1: Get the total number of items
number_of_items = int(input())

# Step 2: Create a list to track active items
is_active = [True] * number_of_items

# Step 3: Initialize current_position and step_count
current_position = 0
step_count = 1

# Step 4: Loop while step_count is less than or equal to 500,000
while step_count <= 500000:
    if is_active[current_position]:  # If the item is active
        is_active[current_position] = False  # Mark it as inactive
    
    step_count += 1  # Increment step_count
    current_position = (current_position + step_count) % number_of_items  # Update position with wrap-around

# Step 5: Create a list of remaining active items
remaining_active_items = [item for item in is_active if item]

# Step 6: Check the length of remaining active items
if len(remaining_active_items) == 0:
    print("YES")
else:
    print("NO")
