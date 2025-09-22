def mark_inactive_elements():
    # Step 2: Read input for total elements
    total_elements = int(input())
    
    # Step 3: Initialize the isActive list
    is_active = [True] * total_elements  # List of active elements initialized to True
    index = 0  # Tracks the current position
    step = 1   # Tracks the number of steps

    # Step 4: Begin the loop to mark elements as inactive
    while step <= 500000:
        if is_active[index]:  # Check if the current element is still active
            is_active[index] = False  # Mark it as inactive
        step += 1  # Increment the step
        index = (index + step) % total_elements  # Update index and wrap around

    # Step 5: Filter for remaining active elements
    active_elements = [element for element in is_active if element]

    # Step 6: Output the result
    if len(active_elements) == 0:
        print("YES")  # All elements are inactive
    else:
        print("NO")   # There are still active elements

# Call the function to execute the logic
mark_inactive_elements()
