def doMain():
    # Prompt the user for the first sequence of numbers
    firstInput = input()
    
    # Prompt the user for the second sequence of numbers
    secondInput = input()
    
    # Split the input sequences into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize the difference counter
    differenceCount = 0
    
    # Compare corresponding numbers, up to the third number
    for i in range(min(3, len(firstList), len(secondList))):
        # Convert the current number to integers
        firstNumber = int(firstList[i])
        secondNumber = int(secondList[i])
        
        # If the numbers are different, increment the difference counter
        if firstNumber != secondNumber:
            differenceCount += 1
            
    # Check the difference count and output the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
doMain()
