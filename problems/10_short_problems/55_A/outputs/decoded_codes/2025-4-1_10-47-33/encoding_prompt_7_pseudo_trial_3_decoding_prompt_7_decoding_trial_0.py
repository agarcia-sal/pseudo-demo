def checkAllNumbersRemoved(n):
    # Initialize a list to track removals, setting all elements to True initially
    isRemoved = [True] * n
    # Initialize the current index and step variables
    currentIndex = 0
    currentStep = 1

    # Continue processing until we've reached the maximum step limit
    while currentStep <= 500000:
        # If the current index has not been removed, mark it as removed
        if isRemoved[currentIndex]:
            isRemoved[currentIndex] = False
        
        # Increment the step count
        currentStep += 1
        # Update the current index based on the step size
        currentIndex = (currentIndex + currentStep) % n

    # Gather all remaining indices that are still marked as True
    remaining = [removed for removed in isRemoved if removed]

    # Depending on whether we have any remaining True elements, print the result
    if len(remaining) == 0:
        print('YES')
    else:
        print('NO')

# Sample input reading and function execution
n = int(input())
checkAllNumbersRemoved(n)
