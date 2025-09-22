def doMain():
    # Prompt user for the first input sequence and store it
    firstInput = input()
    # Prompt user for the second input sequence and store it
    secondInput = input()
    
    # Split the input sequences into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for the differences
    differenceCount = 0
    
    # Compare corresponding numbers from each list (only up to the third number)
    for i in range(min(3, len(firstList), len(secondList))):
        firstNumber = int(firstList[i])
        secondNumber = int(secondList[i])
        
        # Increment differenceCount if numbers are not equal
        if firstNumber != secondNumber:
            differenceCount += 1
    
    # Check the count of differences and output accordingly
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
doMain()
