# Start of the program
def checkVisibility():
    # Read input value
    totalCount = int(input())  # Read an integer from input

    # Create a boolean list initialized to True
    visibilityList = [True] * totalCount  # List initialized with True values

    # Initialize the index and iteration counter
    currentIndex = 0
    stepCounter = 1

    # Loop until the step counter exceeds 500,000
    while stepCounter <= 500000:
        # If the current visibility status is True
        if visibilityList[currentIndex] == True:
            # Mark the current position as False (not visible)
            visibilityList[currentIndex] = False

        # Increment the step counter
        stepCounter += 1

        # Update current index based on the step counter
        currentIndex = (currentIndex + stepCounter) % totalCount

    # Create a list of visible indices
    visibleList = [i for i in visibilityList if i]  # List containing elements that are True

    # Check if there are any visible positions remaining
    if len(visibleList) == 0:
        print("YES")  # All positions are not visible
    else:
        print("NO")   # There are still visible positions

# Call the function to run the program
checkVisibility()
