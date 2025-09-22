def doMain():
    # Step 1: Input Handling
    inputFirstLine = input()
    inputSecondLine = input()
    
    # Split the input into lists
    firstList = inputFirstLine.split()
    secondList = inputSecondLine.split()
    
    # Step 2: Initialize a Counter
    differenceCount = 0  # This will track the number of differing elements
    
    # Step 3: Comparison Loop
    for index in range(3):  # Iterate over the first three elements
        firstValue = int(firstList[index])       # Convert first list value to int
        secondValue = int(secondList[index])     # Convert second list value to int
        
        if firstValue != secondValue:
            differenceCount += 1  # Increment counter if the values differ
    
    # Step 4: Output Decision
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 5: Function Invocation
doMain()
