def doMain():
    # Step 1: Input Handling
    inputFirstLine = input()
    inputSecondLine = input()
    
    # Split input lines into lists
    firstList = inputFirstLine.split()
    secondList = inputSecondLine.split()
    
    # Step 2: Initialize a Counter
    differenceCount = 0
    
    # Step 3: Comparison Loop
    for index in range(3):  # Comparing first three elements
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if values are different
        if firstValue != secondValue:
            differenceCount += 1
            
    # Step 4: Output Decision
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 5: Function Invocation
doMain()
