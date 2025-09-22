# Function to determine if all items in the list are marked as False
def marking_process():
    # Step 1: Read input for total number of elements
    n = int(input())
    
    # Step 2: Initialize the markings list with all elements set to True
    markings = [True] * n
    
    # Step 3: Initialize variables
    index = 0   # tracks the current position in the markings list
    step = 1    # indicates the current counting step

    # Step 4: Start the marking process
    while step <= 500000:
        # Check if the current item is True
        if markings[index]:
            # Mark the current item as False
            markings[index] = False
        
        # Increment step
        step += 1
        # Update the index to the new position wrapping around using modulo n
        index = (index + step) % n

    # Step 5: Check for remaining True items in the markings list
    remainingTrue = [mark for mark in markings if mark]

    # Step 6: Output result based on remaining True items
    if len(remainingTrue) == 0:
        print("YES")  # All items were marked as False
    else:
        print("NO")   # There is at least one item that remains True

# Calling the function to execute the marking process
marking_process()
