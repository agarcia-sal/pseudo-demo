# Start by getting an integer input that represents the total number of items
number_of_items = int(input())

# Create a list called is_active with number_of_items elements, initialized to True
is_active = [True] * number_of_items

# Initialize current_position and step_count
current_position = 0
step_count = 1

# Loop until step_count exceeds 500,000
while step_count <= 500000:
    # Check if the item at current_position is still active
    if is_active[current_position]:
        # Mark this item as inactive
        is_active[current_position] = False
        
        # Increment the step count
        step_count += 1
        
        # Update current_position with the new value
        current_position = (current_position + step_count) % number_of_items
    else:
        # If the item is inactive, just move to the next step without incrementing step_count
        current_position = (current_position + 1) % number_of_items

# Create a list of remaining active items based on the is_active list
remaining_active_items = [index for index, active in enumerate(is_active) if active]

# Check the length of remaining_active_items
if len(remaining_active_items) == 0:
    print("YES")
else:
    print("NO")
