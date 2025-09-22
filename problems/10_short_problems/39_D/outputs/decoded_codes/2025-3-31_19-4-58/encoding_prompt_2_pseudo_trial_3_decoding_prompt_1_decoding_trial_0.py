# Start of Program

def doMain():
    # Prompt the user to enter the first sequence of numbers
    firstInput = input()
    # Prompt the user to enter the second sequence of numbers
    secondInput = input()
    
    # Split Input Sequences
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize Difference Counter
    differenceCount = 0
    
    # Compare Corresponding Numbers
    for i in range(min(3, len(firstList), len(secondList))):  # Compare up to the third number or whichever list is shorter
        firstNumber = int(firstList[i])  # Convert current number to integer
        secondNumber = int(secondList[i])  # Convert current number to integer
        
        if firstNumber != secondNumber:  # If the numbers are not equal
            differenceCount += 1  # Increase the difference count
    
    # Check Difference Count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main Program Execution
doMain()

# End of Program
