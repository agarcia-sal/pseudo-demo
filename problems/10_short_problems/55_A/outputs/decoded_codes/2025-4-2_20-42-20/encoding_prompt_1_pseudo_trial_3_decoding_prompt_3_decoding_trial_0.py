def process_elements():
    # Step 1: Input the number of elements
    n = int(input())
    
    # Step 2: Initialize the tracking list and variables
    is_true = [True] * n  # List to track statuses
    current_index = 0
    step = 1

    # Step 3: Loop until the step exceeds 500,000
    while step <= 500000:
        # Check the value at the current index
        if is_true[current_index]:
            is_true[current_index] = False  # Mark as False if True
        
        # Increment step and compute new current index
        step += 1
        current_index = (current_index + step) % n  # Update the index wrapping around

    # Step 4: Filter out the remaining True values
    remaining_true = [status for status in is_true if status]

    # Step 5: Check outcome
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Run the function to execute the logic
process_elements()
