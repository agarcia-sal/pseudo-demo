def main():
    # Step 1: Get the total number of items
    number_of_items = int(input())
    
    # Step 2: Initialize the list to keep track of active items
    is_active = [True] * number_of_items
    
    # Step 3: Initialize current position and step count
    current_position = 0
    step_count = 1
    
    # Step 4: Loop while step_count is less than or equal to 500,000
    while step_count <= 500000:
        if is_active[current_position]:  # Check if the current item is active
            is_active[current_position] = False  # Mark it as inactive
            step_count += 1  # Increment the step count
            current_position = (current_position + step_count) % number_of_items  # Update the current position
        else:
            current_position = (current_position + 1) % number_of_items  # Move to the next item if inactive

    # Step 5: Collect remaining active items
    remaining_active_items = [item for item in is_active if item]
    
    # Step 6: Check the length of remaining active items and output the result
    if len(remaining_active_items) == 0:
        print("YES")  # All items are inactive
    else:
        print("NO")  # There are still active items

# Run the main function
main()
