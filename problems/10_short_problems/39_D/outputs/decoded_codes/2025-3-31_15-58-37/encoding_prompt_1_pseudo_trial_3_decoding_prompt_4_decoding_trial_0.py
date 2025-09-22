def doMain():
    # Step 2: Input Handling
    firstInput = input()
    secondInput = input()
    
    # Step 3: Split the inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 4: Initialize Counter
    differenceCount = 0

    # Step 5: Comparison Loop
    for index in range(3):  # Loop through the first three indices (0 to 2)
        valueA = int(firstList[index])  # Convert first list value to integer
        valueB = int(secondList[index])  # Convert second list value to integer
        
        if valueA != valueB:  # Check if the values differ
            differenceCount += 1  # Increment the difference count if they are not equal

    # Step 6: Decision Making
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Step 7: Execution Block
if __name__ == "__main__":
    doMain()


Input:
1 2 3
1 2 4

Output:
YES
