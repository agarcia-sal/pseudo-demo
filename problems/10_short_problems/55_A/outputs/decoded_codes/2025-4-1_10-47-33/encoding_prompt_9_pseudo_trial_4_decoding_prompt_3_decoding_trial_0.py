def can_all_elements_be_marked():
    # Step 1: Read Input
    n = int(input())
    
    # Step 2: Initialize List
    marked = [True] * n  # List to keep track of marked positions

    # Step 3: Initialize Counters
    current_index = 0
    step_size = 1

    # Step 4: Iterative Marking
    while step_size <= 500000:
        if marked[current_index]:  # Check if the current position is still marked
            marked[current_index] = False  # Mark it as false
        step_size += 1  # Increment the step size
        current_index = (current_index + step_size) % n  # Calculate the next index

    # Step 5: Check Marks
    remaining_true = [marked[i] for i in range(n) if marked[i]]

    # Step 6: Output Result
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
can_all_elements_be_marked()
