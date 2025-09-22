def doMain():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split input lines into lists of strings
    firstList = firstLine.split()
    secondList = secondLine.split()
    
    # Initialize the result counter
    mismatchCount = 0
    
    # Iterate over the first three elements of both lists
    for index in range(3):  # Adjusted for Python's 0-indexing
        # Convert string elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check for mismatches
        if firstValue != secondValue:
            mismatchCount += 1  # Increment the mismatch counter

    # Determine the output based on mismatch count
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    doMain()
