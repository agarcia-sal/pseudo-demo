def check_visibility():
    # Read input value
    total_count = int(input())
    
    # Create a boolean list initialized to True
    visibility_list = [True] * total_count

    # Initialize the index and iteration counter
    current_index = 0
    step_counter = 1

    # Loop until the step counter exceeds 500,000
    while step_counter <= 500000:
        # If the current visibility status is True
        if visibility_list[current_index]:
            # Mark the current position as False (not visible)
            visibility_list[current_index] = False
        
        # Increment the step counter
        step_counter += 1

        # Update current index based on the step counter
        current_index = (current_index + step_counter) % total_count

    # Create a list of visible indices
    visible_list = [index for index, is_visible in enumerate(visibility_list) if is_visible]

    # Check if there are any visible positions remaining
    if len(visible_list) == 0:
        print("YES")  # All positions are not visible
    else:
        print("NO")   # There are still visible positions

# Call the function to execute the logic
check_visibility()
