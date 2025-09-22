def doMain():
    # Input Handling
    inputFirstLine = input()
    inputSecondLine = input()
    
    # Split the inputs into lists
    firstList = inputFirstLine.split()
    secondList = inputSecondLine.split()

    # Initialize a Counter
    differenceCount = 0

    # Comparison Loop
    for index in range(3):  # Check the first three elements
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        if firstValue != secondValue:
            differenceCount += 1

    # Output Decision
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Function Invocation
doMain()
