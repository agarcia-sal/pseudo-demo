def doMain():
    # Prompt the user for the first sequence of numbers
    firstInput = input()
    
    # Prompt the user for the second sequence of numbers
    secondInput = input()
    
    # Split input sequences into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize difference counter
    differenceCount = 0
    
    # Compare the corresponding numbers (up to the third number)
    for i in range(min(len(firstList), len(secondList), 3)):
        firstNumber = int(firstList[i])
        secondNumber = int(secondList[i])
        
        # Check if numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1
    
    # Check if difference count is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
doMain()


   1 2 3
   1 2 4
   

   1 2 3
   4 5 6
   

   1 2
   1 3
   

   1
   2
   