def checkCondition(inputNumber):
    # Initialize a list of boolean values indicating status for each index
    booleanList = [True] * inputNumber  # Create a list filled with True
    indexJ = 0  # Initialize indexJ
    indexI = 1  # Initialize indexI

    # Loop while indexI is less than or equal to 500000
    while indexI <= 500000:
        # Check if the current position in booleanList is True
        if booleanList[indexJ]:
            # Mark the current position as False
            booleanList[indexJ] = False

        # Increment indexI
        indexI += 1

        # Update indexJ using modular arithmetic for cycling through the array
        indexJ = (indexJ + indexI) % inputNumber

    # Filter booleanList for positions that are still True
    trueValues = [i for i in range(inputNumber) if booleanList[i]]

    # Check if there are any True values left in the filtered list
    if len(trueValues) == 0:
        print('YES')  # Output indicates condition is satisfied
    else:
        print('NO')   # Output indicates condition is not satisfied

# Example to test the function
inputNumber = int(input())
checkCondition(inputNumber)
