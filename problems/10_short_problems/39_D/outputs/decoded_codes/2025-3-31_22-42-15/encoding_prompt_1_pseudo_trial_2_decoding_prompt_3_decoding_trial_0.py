def doMain():
    # Step 1: Get Input Values
    firstInput = input()
    secondInput = input()
    
    # Step 2: Split Input into Lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Step 3: Initialize the Difference Counter
    differenceCount = 0
    
    # Step 4: Iterate and Count Differences
    for index in range(3):  # Loop from 0 to 2
        valueA = int(firstValues[index])
        valueB = int(secondValues[index])
        
        if valueA != valueB:
            differenceCount += 1
    
    # Step 5: Decide Output Based on Count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Run Main Function if Script is Executed
if __name__ == "__main__":
    doMain()
