def elimination_process():
    # Step 1: Initialize Input
    numberOfElements = int(input())

    # Step 2: Create a Boolean List
    isActive = [True] * numberOfElements

    # Step 3: Set Initial Indices
    currentIndex = 0
    stepSize = 1

    # Step 4: Start Elimination Process
    while stepSize <= 500000:
        if isActive[currentIndex]:
            isActive[currentIndex] = False  # Mark the current position as eliminated
        
        stepSize += 1  # Increment the step size
        currentIndex = (currentIndex + stepSize) % numberOfElements  # Update the current index

    # Step 5: Check Remaining Active Entries
    remainingActive = [active for active in isActive if active]

    # Step 6: Determine and Print Final Result
    if len(remainingActive) == 0:
        print("YES")  # All positions have been eliminated
    else:
        print("NO")   # Some positions are still active
