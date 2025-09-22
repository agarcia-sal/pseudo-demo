# Start the program

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
    
    # For each index from 0 to 2 (inclusive):
    for index in range(3):
        # Retrieve the value from firstList at the current index and convert it to an integer
        firstValue = int(firstList[index])
        
        # Retrieve the value from secondList at the current index and convert it to an integer
        secondValue = int(secondList[index])
        
        # If firstValue is not equal to secondValue:
        if firstValue != secondValue:
            # Increment mismatchCount by 1
            mismatchCount += 1
    
    # If mismatchCount is less than 3:
    if mismatchCount < 3:
        # Output "YES"
        print("YES")
    # Otherwise:
    else:
        # Output "NO"
        print("NO")

# If this script is being run directly (not imported as a module):
if __name__ == "__main__":
    doMain()  # Call the doMain function to begin execution of the program.
