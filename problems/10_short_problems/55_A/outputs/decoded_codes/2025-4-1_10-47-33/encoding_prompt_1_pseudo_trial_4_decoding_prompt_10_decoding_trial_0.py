def process_array():
    # Step 1: Read integer input from user
    n = int(input())
    
    # Step 2: Initialize a boolean array of size n, all elements set to True
    is_true = [True] * n
    
    # Step 3: Set initial variables
    current_index = 0
    increment = 1

    # Step 4: Loop while increment is less than or equal to 500000
    while increment <= 500000:
        if is_true[current_index]:
            is_true[current_index] = False  # Mark the current index as processed

        increment += 1  # Increment the step
        current_index = (current_index + increment) % n  # Update current index with wrapping

    # Step 5: Check the results
    remaining_true = [status for status in is_true if status]

    # Step 6: Output the result
    if len(remaining_true) == 0:
        print("YES")  # All elements were processed
    else:
        print("NO")   # Some elements remain unprocessed

# Run the function
process_array()
