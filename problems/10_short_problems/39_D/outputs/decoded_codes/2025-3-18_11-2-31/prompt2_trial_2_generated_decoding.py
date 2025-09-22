def doMain():
    # Input Handling
    firstInput = input()
    secondInput = input()
    
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize differenceCount
    differenceCount = 0

    # Comparison Loop
    for index in range(3):  # loop from 0 to 2 inclusive
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        if firstValue != secondValue:
            differenceCount += 1

    # Output Decision
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execution Trigger
if __name__ == "__main__":
    doMain()
