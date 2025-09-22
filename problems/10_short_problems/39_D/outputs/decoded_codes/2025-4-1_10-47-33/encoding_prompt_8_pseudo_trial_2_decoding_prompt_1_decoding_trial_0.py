def compareThreeIntegers():
    # Input Handling
    firstInput = input()
    secondInput = input()

    # Data Processing
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize Difference Counter
    differenceCount = 0

    # Comparison Loop
    for index in range(3):  # Loop from 0 to 2 inclusive
        firstValue = int(firstList[index])  # Convert string to int
        secondValue = int(secondList[index])  # Convert string to int

        # Check if the values differ
        if firstValue != secondValue:
            differenceCount += 1  # Increment the difference count

    # Condition Check
    if differenceCount < 3:
        print("YES")  # Output "YES"
    else:
        print("NO")   # Output "NO"

# Execution
compareThreeIntegers()
