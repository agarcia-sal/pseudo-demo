def check_active_positions():
    # Step 1: Read input
    n = int(input())  # Input for the size of the list

    # Step 2: Initialize list
    isActive = [True] * n  # All positions start as active (True)

    # Step 3: Set counters
    currentPosition = 0  # Starting position
    stepCount = 1  # Step size for the iterations

    # Step 4: Loop until condition met
    while stepCount <= 500000:
        if isActive[currentPosition]:  # Check if current position is active
            isActive[currentPosition] = False  # Mark as inactive
        stepCount += 1  # Increment step count
        currentPosition = (currentPosition + stepCount) % n  # Update current position with wrap-around

    # Step 5: Check active positions
    inactivePositions = [i for i in range(n) if isActive[i]]  # List of positions that are still active

    # Step 6: Output result
    if not inactivePositions:  # Check if there are no active positions
        print("YES")  # All positions marked inactive
    else:
        print("NO")  # At least one position still active

# Example call to the function
check_active_positions()
