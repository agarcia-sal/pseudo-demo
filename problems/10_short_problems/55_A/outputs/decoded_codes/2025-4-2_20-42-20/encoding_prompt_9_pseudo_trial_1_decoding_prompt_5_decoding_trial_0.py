# Function to check if all values in a list can be marked as "not true"
def mark_values():
    # Step 1: Read the number of elements
    total_elements = int(input())
    
    # Step 2: Initialize the markings list with all values set to True
    markings = [True] * total_elements
    
    # Step 3: Initialize index and step
    index = 0
    step = 1
    
    # Step 4: Start the marking process
    while step <= 500000:
        # If current index in markings is True
        if markings[index]:
            # Mark it as False
            markings[index] = False
        
        # Increment the step
        step += 1
        
        # Update index circularly to wrap around the list
        index = (index + step) % total_elements
    
    # Step 5: Check remaining marked items
    remaining_true = [mark for mark in markings if mark]
    
    # Step 6: Output result
    if len(remaining_true) == 0:
        print("YES")  # All items are marked as False
    else:
        print("NO")   # At least one item remains True

# Call the function to execute
mark_values()
