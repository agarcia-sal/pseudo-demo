# Step 2: Define a Function `doMain`
def doMain():
    # Step 3: Receive Input
    firstInput = input()
    secondInput = input()
    
    # Step 4: Process Input
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Step 5: Initialize a Counter
    differenceCount = 0
    
    # Step 6: Compare Elements of the Lists
    for i in range(3):  # Loop from index 0 to 2
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        if firstValue != secondValue:
            differenceCount += 1
    
    # Step 7: Determine and Output Result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute the Main Function
if __name__ == "__main__":
    doMain()
