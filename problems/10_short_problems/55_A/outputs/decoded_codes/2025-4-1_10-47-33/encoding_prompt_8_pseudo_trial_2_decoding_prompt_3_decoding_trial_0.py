def determine_active_elements():
    # Step 1: Get input
    n = int(input())  # Read the size of the boolean list

    # Step 2: Initialize list
    isActive = [True] * n  # Create a list of size n with all elements set to True

    # Step 3: Initialize counters
    currentIndex = 0
    stepNumber = 1

    # Step 4: Iterate to modify list
    while stepNumber <= 500000:
        if isActive[currentIndex]:  # If the current position is True
            isActive[currentIndex] = False  # Set it to False
        
        # Update the counters
        stepNumber += 1
        currentIndex = (currentIndex + stepNumber) % n  # Wrap around using modulo n

    # Step 5: Check remaining active elements
    remainingActive = [active for active in isActive if active]  # List of remaining True elements

    # Step 6: Determine output
    if len(remainingActive) == 0:
        print("YES")  # All elements have been set to False
    else:
        print("NO")  # At least one element is still True

# Call the function to run the code
determine_active_elements()
