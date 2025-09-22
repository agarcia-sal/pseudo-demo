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
    for i in range(3):  # Loop over indices 0 to 2
        firstValue = int(firstInputList[i])  # Convert to integer
        secondValue = int(secondInputList[i])  # Convert to integer
        
        if firstValue != secondValue:  # Step 5 condition
            differenceCount += 1  # Increment difference count
            
    # Step 6: Result Evaluation
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execution Trigger
if __name__ == "__main__":
    doMain()
