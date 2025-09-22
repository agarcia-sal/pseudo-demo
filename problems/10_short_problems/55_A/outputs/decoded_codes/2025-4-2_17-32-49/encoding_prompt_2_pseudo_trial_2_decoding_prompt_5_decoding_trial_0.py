# Function to determine if all items are inactive after a series of steps
def check_items_inactivity():
    # Step 1: Get the total number of items from user input
    number_of_items = int(input())
    
    # Step 2: Create a list to track active items, initialized to True
    is_active = [True] * number_of_items
    
    # Step 3: Initialize current position and step count
    current_position = 0
    step_count = 1
    
    # Step 4: Loop to update the status of items
    while step_count <= 500000:
        # Check if the current item is still active
        if is_active[current_position]:
            # Mark the item as inactive
            is_active[current_position] = False
            
            # Increment step count
            step_count += 1
            
            # Update the current position with wrapping around using modulus
            current_position = (current_position + step_count) % number_of_items
    
    # Step 5: Create a list of remaining active items
    remaining_active_items = [item for item in is_active if item]

    # Step 6: Output based on the number of active items
    if len(remaining_active_items) == 0:
        print("YES")
    else:
        print("NO")

# Uncomment the line below to test the function
# check_items_inactivity()
