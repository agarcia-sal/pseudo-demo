def checkIfAllPositionsAreFalse(n):
    # Create a list of boolean values initialized to True
    booleanList = [True] * n

    # Initialize necessary indices
    index = 0
    step = 1

    # Loop until the step exceeds 500,000
    while step <= 500000:
        # If the current index in the boolean list is True
        if booleanList[index] is True:
            # Set the current position to False
            booleanList[index] = False
        
        # Move to the next step
        step += 1
        
        # Calculate the next index based on current index and step size
        index = (index + step) % n

    # Check for remaining True positions in the boolean list
    remainingTruePositions = [i for i, v in enumerate(booleanList) if v]

    # Check if there are no remaining True positions
    if len(remainingTruePositions) == 0:
        print('YES')  # All positions are marked False
    else:
        print('NO')   # There are some positions still marked True

# Sample invocation (not to be included in the function)
n = int(input())
checkIfAllPositionsAreFalse(n)
