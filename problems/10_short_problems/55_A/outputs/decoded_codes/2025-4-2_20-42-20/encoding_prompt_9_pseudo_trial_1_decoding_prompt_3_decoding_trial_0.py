def marking_process():
    # Step 1: Read input
    n = int(input())
    
    # Step 2: Initialize the marking list
    markings = [True] * n
    
    # Step 3: Set initial variables
    index = 0
    step = 1
    
    # Step 4: Start the marking process
    while step <= 500000:
        if markings[index]:  # If the current item is True
            markings[index] = False  # Mark it as False (processed)
        
        step += 1  # Increment the step
        index = (index + step) % n  # Update index for the next position
    
    # Step 5: Check remaining marked items
    remaining_true = [mark for mark in markings if mark]  # List of unmarked items

    # Step 6: Output result
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to run the marking process
marking_process()
