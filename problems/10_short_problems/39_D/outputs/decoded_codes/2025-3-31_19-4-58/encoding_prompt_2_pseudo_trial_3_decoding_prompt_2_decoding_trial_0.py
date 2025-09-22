def doMain():
    # Prompt the user to enter the first sequence of numbers
    firstInput = input()
    
    # Prompt the user to enter the second sequence of numbers
    secondInput = input()
    
    # Split Input Sequences into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize Difference Counter
    differenceCount = 0
    
    # Compare Corresponding Numbers
    for i in range(min(3, len(firstList), len(secondList))):
        firstNumber = int(firstList[i])  # Convert to integer
        secondNumber = int(secondList[i])  # Convert to integer
        
        if firstNumber != secondNumber:
            differenceCount += 1  # Increase the difference count if numbers are not equal
    
    # Check Difference Count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main Program Execution
doMain()
