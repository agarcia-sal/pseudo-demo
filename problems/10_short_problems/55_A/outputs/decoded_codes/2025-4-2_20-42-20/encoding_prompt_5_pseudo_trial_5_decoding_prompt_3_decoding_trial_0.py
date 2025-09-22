def check_active_elements():
    # Step 1: Get Number of Elements
    n = int(input())  # Read an integer value for the number of elements
    
    # Step 2: Initialize List
    isActive = [True] * n  # Create a list with all elements set to True
    
    # Step 3: Set Initial Indices
    currentIndex = 0  # Pointer to the current element
    step = 1  # Step variable
    
    # Step 4: Process the List
    while step <= 500000:
        if isActive[currentIndex]:  # Check if the current element is still active
            isActive[currentIndex] = False  # Deactivate the current element
        
        # Increment step for the next iteration
        step += 1
        
        # Update current index cyclically
        currentIndex = (currentIndex + step) % n  # Wrap around using modulo
    
    # Step 5: Check Remaining Active Elements
    remainingActive = [active for active in isActive if active]  # Filter out active elements
    
    # Step 6: Output Result
    if len(remainingActive) == 0:  # If no active elements left
        print("YES")
    else:
        print("NO")

# To use the function, call check_active_elements()
check_active_elements()
