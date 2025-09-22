def doMain():
    # Read the first input line and store it as firstInput
    firstInput = input()
    
    # Read the second input line and store it as secondInput
    secondInput = input()
    
    # Split firstInput into a list of strings
    firstList = firstInput.split()
    
    # Split secondInput into a list of strings
    secondList = secondInput.split()
    
    # Initialize a variable mismatchCount to zero to keep track of differences
    mismatchCount = 0
    
    # For each index from 0 to 2 (inclusive)
    for index in range(3):
        # Convert values to integers for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # If firstValue is not equal to secondValue, increment mismatchCount
        if firstValue != secondValue:
            mismatchCount += 1
    
    # If mismatchCount is less than 3, output "YES"
    if mismatchCount < 3:
        print("YES")
    # Otherwise, output "NO"
    else:
        print("NO")

# If this script is being run directly
if __name__ == "__main__":
    doMain()
