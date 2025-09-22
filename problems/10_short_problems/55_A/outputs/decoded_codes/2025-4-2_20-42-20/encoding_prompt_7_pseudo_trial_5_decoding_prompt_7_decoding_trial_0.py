def checkRemainingTrueValues():
    # Read an integer input specifying the number of elements in the boolean array
    totalElements = int(input())

    # Initialize a boolean array filled with True values
    booleanArray = [True] * totalElements

    # Initialize index variables
    currentIndex = 0
    stepCounter = 1

    # Loop while stepCounter is less than or equal to 500000
    while stepCounter <= 500000:
        # Check if the current index has a True value
        if booleanArray[currentIndex]:
            # Set the value at the current index to False
            booleanArray[currentIndex] = False
            
        # Increment stepCounter
        stepCounter += 1

        # Calculate the new index using the stepCounter
        currentIndex = (currentIndex + stepCounter) % totalElements

    # Create a list of all remaining True values in the boolean array
    remainingTrueValues = [value for value in booleanArray if value]

    # Check if there are any True values remaining
    if len(remainingTrueValues) == 0:
        print('YES')
    else:
        print('NO')

# The function is invoked without any parameters; it reads input directly.
checkRemainingTrueValues()
