def doMain():
    # Prompt user to enter the first sequence of numbers
    firstInput = input()
    # Prompt user to enter the second sequence of numbers
    secondInput = input()
    
    # Split input sequences into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize difference counter
    differenceCount = 0
    
    # Compare corresponding numbers in the two lists, up to the third number
    for i in range(min(3, len(firstList), len(secondList))):  
        # Convert current numbers to integers
        firstNumber = int(firstList[i])
        secondNumber = int(secondList[i])
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1
    
    # Check the difference count and output result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
doMain()
