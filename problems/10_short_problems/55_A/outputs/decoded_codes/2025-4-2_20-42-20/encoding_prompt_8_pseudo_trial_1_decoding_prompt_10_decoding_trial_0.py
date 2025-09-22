def determine_activity_status():
    # Step 1: Read input
    n = int(input())
    
    # Step 2: Initialize list of active statuses
    isActive = [True] * n  # Create a list filled with True
    
    # Step 3: Set counters
    currentPosition = 0
    stepCount = 1
    
    # Step 4: Loop until stepCount exceeds 500,000
    while stepCount <= 500000:
        if isActive[currentPosition]:  # Check if the current position is active
            isActive[currentPosition] = False  # Mark this position as inactive
        
        stepCount += 1  # Increment stepCount
        currentPosition = (currentPosition + stepCount) % n  # Update currentPosition with wrap-around
    
    # Step 5: Check for active positions
    inactivePositions = [index for index, status in enumerate(isActive) if status]
    
    # Step 6: Output the result
    if not inactivePositions:  # If the list of inactive positions is empty
        print("YES")  # All positions are inactive
    else:
        print("NO")  # At least one position is still active

# Call the function to execute
determine_activity_status()
