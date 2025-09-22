def doMain():
    # Input Collection
    firstInputString = input()
    secondInputString = input()

    # String Splitting
    firstInputList = firstInputString.split()
    secondInputList = secondInputString.split()

    # Result Initialization
    differenceCount = 0

    # Comparison Loop
    for i in range(3):  # Iterating through the first three elements
        firstValue = int(firstInputList[i])
        secondValue = int(secondInputList[i])
        
        if firstValue != secondValue:
            differenceCount += 1

    # Result Evaluation
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execution Trigger
if __name__ == "__main__":
    doMain()
