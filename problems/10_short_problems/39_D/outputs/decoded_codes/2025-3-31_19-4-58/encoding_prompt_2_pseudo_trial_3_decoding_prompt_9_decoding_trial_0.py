def doMain():
    # Prompt the user to enter the first sequence of numbers
    firstInput = input()
    # Prompt the user to enter the second sequence of numbers
    secondInput = input()
    
    # Split the input sequences into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize the difference counter
    differenceCount = 0

    # Compare corresponding numbers up to the third number
    for i in range(min(3, len(firstList), len(secondList))):
        firstNumber = int(firstList[i])  # Convert to integer
        secondNumber = int(secondList[i])  # Convert to integer
        
        # If the numbers are different, increase the differenceCount
        if firstNumber != secondNumber:
            differenceCount += 1

    # Check the difference count and output the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
doMain()
