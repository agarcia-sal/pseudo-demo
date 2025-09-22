def doMain():
    # Step 2: Input Collection
    firstInputString = input()
    secondInputString = input()

    # Step 3: String Splitting
    firstInputList = firstInputString.split()
    secondInputList = secondInputString.split()

    # Step 4: Result Initialization
    differenceCount = 0

    # Step 5: Comparison Loop
    for index in range(3):  # We only compare the first three elements
        firstValue = int(firstInputList[index])
        secondValue = int(secondInputList[index])
        
        if firstValue != secondValue:
            differenceCount += 1

    # Step 6: Result Evaluation
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execution Trigger
if __name__ == "__main__":
    doMain()
