def doMain():
    # Input Handling
    inputFirstLine = input()
    inputSecondLine = input()
    
    # Split the inputs into lists
    firstList = inputFirstLine.split()
    secondList = inputSecondLine.split()
    
    # Initialize a Counter for different elements
    differenceCount = 0
    
    # Comparison Loop
    for index in range(3):  # We are only interested in the first three elements
        firstValue = int(firstList[index])   # Convert first list element to integer
        secondValue = int(secondList[index])  # Convert second list element to integer
        
        # Check for differences
        if firstValue != secondValue:
            differenceCount += 1  # Increment count if values differ
    
    # Output Decision
    if differenceCount < 3:
        print("YES")  # Print "YES" if differences are less than 3
    else:
        print("NO")   # Print "NO" if differences are 3 or more

# Function Invocation
doMain()
