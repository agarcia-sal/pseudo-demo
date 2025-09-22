def doMain():
    # Input handling
    inputFirstLine = input()  # Read the first line of input
    inputSecondLine = input()  # Read the second line of input
    
    # Split the input lines into lists
    firstList = inputFirstLine.split()  # List from the first line
    secondList = inputSecondLine.split()  # List from the second line
    
    # Initialize a counter for different elements
    differenceCount = 0  # Counter for differing elements

    # Comparison loop for the first three elements
    for index in range(3):  # We only compare the first three elements
        # Convert string values to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Increment the counter if values differ
        if firstValue != secondValue:
            differenceCount += 1

    # Output decision based on the number of differences
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Function invocation
doMain()
