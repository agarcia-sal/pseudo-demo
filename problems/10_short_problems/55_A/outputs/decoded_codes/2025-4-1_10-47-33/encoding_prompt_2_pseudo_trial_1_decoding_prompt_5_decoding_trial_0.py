# Function to determine the elimination outcome based on user input

def elimination_process():
    # Step 1: Initialize Input
    number_of_elements = int(input())  # Read an integer value for the number of elements

    # Step 2: Create a Boolean List
    is_active = [True] * number_of_elements  # List to track active elements

    # Step 3: Set Initial Indices
    current_index = 0  # Starting position
    step_size = 1      # Initial step size for elimination

    # Step 4: Start Elimination Process
    while step_size <= 500000:
        if is_active[current_index]:    # Check if the current element is active
            is_active[current_index] = False  # Mark the current element as eliminated
        step_size += 1  # Increment step size for the next round
        current_index = (current_index + step_size) % number_of_elements  # Update index with wrap-around

    # Step 5: Check Remaining Active Entries
    remaining_active = [active for active in is_active if active]  # Collect all active elements

    # Step 6: Determine and Print Final Result
    if len(remaining_active) == 0:
        print("YES")  # All positions have been eliminated
    else:
        print("NO")   # Some positions are still active

# Call the function to execute the elimination process
elimination_process()
