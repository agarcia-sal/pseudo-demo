def doMain():
    # Read the first input line and store it as firstInput
    firstInput = input()
    
    # Read the second input line and store it as secondInput
    secondInput = input()
    
    # Split firstInput into a list of strings and store it as firstList
    firstList = firstInput.split()
    
    # Split secondInput into a list of strings and store it as secondList
    secondList = secondInput.split()
    
    # Initialize a variable mismatchCount to zero to keep track of differences
    mismatchCount = 0
    
    # For each index from 0 to 2 (inclusive)
    for index in range(3):
        # Retrieve and convert values from firstList and secondList
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check for mismatches
        if firstValue != secondValue:
            mismatchCount += 1
    
    # Determine output based on the count of mismatches
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Check if this script is being run directly
if __name__ == "__main__":
    doMain()


1 2 3
1 2 4


1 2 3
4 5 6
