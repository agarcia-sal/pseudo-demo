def process_eliminations():
    # Input: Read the size of the array
    n = int(input())
    
    # Step 1: Initialization
    isAlive = [True] * n  # Create an array of size n with all values set to True
    currentIndex = 0
    stepCount = 1

    # Step 2: Elimination Process
    while stepCount <= 500000:
        if isAlive[currentIndex]:  # If currentIndex is alive
            isAlive[currentIndex] = False  # Mark as eliminated

        # Increment stepCount
        stepCount += 1
        # Update currentIndex making sure it wraps around
        currentIndex = (currentIndex + stepCount) % n

    # Step 3: Final Check
    remaining = [alive for alive in isAlive if alive]  # Collect all still alive
    
    # Output result
    if len(remaining) == 0:
        print("YES")  # No one is alive
    else:
        print("NO")  # There are still people alive
