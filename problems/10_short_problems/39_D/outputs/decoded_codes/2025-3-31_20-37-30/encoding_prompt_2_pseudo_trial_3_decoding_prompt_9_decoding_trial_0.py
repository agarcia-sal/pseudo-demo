def doMain():
    # Input Collection
    firstInputString = input()
    secondInputString = input()

    # String Splitting
    firstInputList = firstInputString.split()
    secondInputList = secondInputString.split()

    # Result Initialization
    differenceCount = 0  # Initialize the difference counter

    # Comparison Loop
    for index in range(3):  # Assuming the input lists have at least 3 elements
        # Convert input strings to integers
        firstValue = int(firstInputList[index])
        secondValue = int(secondInputList[index])
        
        # Increment the difference count if values are not equal
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
