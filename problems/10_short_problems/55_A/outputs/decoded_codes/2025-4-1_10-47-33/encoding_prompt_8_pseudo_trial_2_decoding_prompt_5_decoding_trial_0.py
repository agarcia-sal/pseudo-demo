def check_remaining_active_elements():
    # Get the size of the boolean list from user input
    n = int(input())
    
    # Initialize the list with all elements set to True
    isActive = [True] * n
    
    # Initialize index and step variables
    currentIndex = 0
    stepNumber = 1
    
    # Iterate to modify the list based on the counting sequence
    while stepNumber <= 500000:
        if isActive[currentIndex]:  # Check if the current position is True
            isActive[currentIndex] = False  # Set it to False
        stepNumber += 1  # Increment the step
        currentIndex = (currentIndex + stepNumber) % n  # Update index using modulo
    
    # Collect the remaining active elements
    remainingActive = [active for active in isActive if active]  # Collect True values
    
    # Determine the output based on remaining active elements
    if len(remainingActive) == 0:
        print("YES")  # All elements have been marked False
    else:
        print("NO")   # At least one element remains True

# Example test case: Uncomment the line below to test the function
# check_remaining_active_elements()
