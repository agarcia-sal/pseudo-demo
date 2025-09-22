def doMain():
    # Input Handling
    inputFirstLine = input()
    inputSecondLine = input()
    firstList = inputFirstLine.split()
    secondList = inputSecondLine.split()

    # Initialize a Counter
    differenceCount = 0

    # Comparison Loop
    for index in range(3):  # Looping over the first three elements
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        if firstValue != secondValue:
            differenceCount += 1  # Increase counter if values differ

    # Output Decision
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Function Invocation
doMain()
