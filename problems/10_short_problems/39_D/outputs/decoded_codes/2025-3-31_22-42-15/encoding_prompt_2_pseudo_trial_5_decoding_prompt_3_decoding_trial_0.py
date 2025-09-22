def doMain():
    # Read the first input line and store it as firstInput
    firstInput = input().strip()
    
    # Read the second input line and store it as secondInput
    secondInput = input().strip()
    
    # Split the input lines into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize mismatch count to track differences
    mismatchCount = 0
    
    # Compare each corresponding index in the two lists
    for index in range(3):  # Loop from 0 to 2
        # Convert values from both lists to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Increment mismatchCount if values are not equal
        if firstValue != secondValue:
            mismatchCount += 1
    
    # Output "YES" if mismatches are less than 3, otherwise "NO"
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()
