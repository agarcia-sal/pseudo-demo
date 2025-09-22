def doMain():
    # Get user input for two lines
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists by space
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare elements of the two lists
    for index in range(3):  # Loop through the first three indices
        firstValue = int(firstList[index])  # Convert the first list element to integer
        secondValue = int(secondList[index])  # Convert the second list element to integer
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1  # Increment the counter if they differ
    
    # Determine the output based on the difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the script runs
if __name__ == "__main__":
    doMain()
