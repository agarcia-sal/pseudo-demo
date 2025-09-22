def checkIfAllPositionsAreFalse(n):
    # Create a list of boolean values initialized to True
    booleanList = [True] * n

    # Initialize necessary indices
    index = 0
    step = 1

    # Loop until the step exceeds 500000
    while step <= 500000:
        # If the current index in the boolean list is True
        if booleanList[index] is True:
            # Set the current position to False
            booleanList[index] = False
        
        # Move to the next step
        step += 1
        
        # Calculate the next index based on current index and step size
        index = (index + step) % n

    # Create a list of True positions remaining in the boolean list
    remainingTruePositions = [i for i in range(n) if booleanList[i]]

    # Check if there are no remaining True positions
    if len(remainingTruePositions) == 0:
        print('YES')  # All positions are marked False
    else:
        print('NO')   # There are some positions still marked True

# Example of calling the function (you would call this with actual value of n)
n = int(input())
checkIfAllPositionsAreFalse(n)
