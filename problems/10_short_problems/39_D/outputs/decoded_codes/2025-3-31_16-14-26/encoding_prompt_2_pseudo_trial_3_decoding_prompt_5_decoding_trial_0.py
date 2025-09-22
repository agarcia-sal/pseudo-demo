def doMain():
    # Prompt user for the first set of values and store as 'firstInput'
    firstInput = input()
    # Prompt user for the second set of values and store as 'secondInput'
    secondInput = input()
    
    # Split the input strings into lists of individual string values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a variable to count the number of differing values
    differenceCount = 0
    
    # Loop through the indexes 0 to 2 (for three iterations)
    for i in range(3):
        # Convert current index values to integers
        firstValue = int(firstValues[i])
        secondValue = int(secondValues[i])
        
        # Compare the two integer values
        if firstValue != secondValue:
            # If they differ, increment the difference count
            differenceCount += 1
    
    # After the loop, check the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Check if the program is run as the main program
if __name__ == "__main__":
    doMain()
