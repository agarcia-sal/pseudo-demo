def checkIfAllPositionsAreFalse(n):
    # Create a list of boolean values initialized to True
    booleanList = [True] * n

    # Initialize necessary indices
    index = 0
    step = 1

    # Loop until the step exceeds 500000
    while step <= 500000:
        # If the current index in the boolean list is True
        if booleanList[index]:
            # Set the current position to False
            booleanList[index] = False
        
        # Move to the next step
        step += 1
        
        # Calculate the next index based on current index and step size
        index = (index + step) % n

    # Check for remaining True positions in the boolean list
    if all(not pos for pos in booleanList):
        print('YES')  # All positions are marked False
    else:
        print('NO')   # There are some positions still marked True

# Example of calling the function (comment out if needed)
# n = int(input())
# checkIfAllPositionsAreFalse(n)


checkIfAllPositionsAreFalse(1)   # Expected output: 'YES'
checkIfAllPositionsAreFalse(2)   # Expected output: 'NO'
checkIfAllPositionsAreFalse(3)   # Expected output: 'NO'
