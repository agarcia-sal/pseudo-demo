def compareThreeIntegers():
    # Prompt user for input and store as firstInput
    firstInput = input()
    # Prompt user for input and store as secondInput
    secondInput = input()
    
    # Split firstInput into a list of strings
    firstList = firstInput.split()
    # Split secondInput into a list of strings
    secondList = secondInput.split()
    
    # Initialize difference counter
    differenceCount = 0

    # Comparison loop for the three integers
    for index in range(3):
        # Convert the item into integer
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if values differ
        if firstValue != secondValue:
            differenceCount += 1

    # Condition check to determine output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the function
compareThreeIntegers()
