# Start the program

def doMain():
    # Step 3: Read the first input line and store it as firstInput
    firstInput = input()
    
    # Step 4: Read the second input line and store it as secondInput
    secondInput = input()
    
    # Step 5: Split firstInput into a list of strings and store it as firstList
    firstList = firstInput.split()
    
    # Step 6: Split secondInput into a list of strings and store it as secondList
    secondList = secondInput.split()
    
    # Step 7: Initialize a variable mismatchCount to zero to keep track of differences
    mismatchCount = 0
    
    # Step 8: For each index from 0 to 2 (inclusive)
    for index in range(3):  # range(3) gives us indices 0, 1, 2
        # Retrieve and convert values from the lists
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # If firstValue is not equal to secondValue
        if firstValue != secondValue:
            # Increment mismatchCount by 1
            mismatchCount += 1
    
    # Step 9: If mismatchCount is less than 3
    if mismatchCount < 3:
        # Output "YES"
        print("YES")
    # Step 10: Otherwise
    else:
        # Output "NO"
        print("NO")

# Step 12: If this script is being run directly (not imported as a module)
if __name__ == "__main__":
    doMain()
