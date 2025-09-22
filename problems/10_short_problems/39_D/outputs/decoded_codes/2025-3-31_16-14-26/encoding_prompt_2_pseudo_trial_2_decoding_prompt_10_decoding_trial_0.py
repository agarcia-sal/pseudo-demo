def doMain():
    # Prompt for the first set of values and store them in firstSet
    firstSet = input()
    
    # Prompt for the second set of values and store them in secondSet
    secondSet = input()

    # Split the input strings into lists of values
    firstList = firstSet.split()
    secondList = secondSet.split()

    # Initialize a counter to keep track of differences
    differenceCount = 0
    
    # Loop through each index from 0 to 2
    for index in range(3):
        # Convert the current index values from strings to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check for differences
        if firstValue != secondValue:
            differenceCount += 1
    
    # Output result based on the difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the script starts
if __name__ == "__main__":
    doMain()
