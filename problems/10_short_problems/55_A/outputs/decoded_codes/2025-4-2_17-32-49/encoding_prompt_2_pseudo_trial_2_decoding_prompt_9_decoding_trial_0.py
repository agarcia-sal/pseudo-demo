# Get the number of items from user input
number_of_items = int(input())

# Create a list with all items initially set to True (active)
is_active = [True] * number_of_items

# Initialize the current position and step count
current_position = 0
step_count = 1

# Loop while step count is less than or equal to 500,000
while step_count <= 500000:
    # Check if the current item is active
    if is_active[current_position]:
        # Mark the item as inactive
        is_active[current_position] = False
        
    # Increment the step count
    step_count += 1
    
    # Update the current position using modulus to wrap around the list
    current_position = (current_position + step_count) % number_of_items

# Create a list of remaining active items
remaining_active_items = [item for item in is_active if item]

# Check the number of remaining active items and print the result
if len(remaining_active_items) == 0:
    print("YES")
else:
    print("NO")
