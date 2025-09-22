def checkRemainingTrueValues(inputNumber):
    # Convert the input into an integer
    totalElements = inputNumber

    # Initialize an array of boolean values all set to True
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

    # Create a list of all True values remaining in the boolean array
    remainingTrueValues = [value for value in booleanArray if value]

    # Check if there are any True values remaining
    if len(remainingTrueValues) == 0:
        print('YES')
    else:
        print('NO')

# Example of calling the function
# Uncomment the following line to test
# checkRemainingTrueValues(int(input()))
