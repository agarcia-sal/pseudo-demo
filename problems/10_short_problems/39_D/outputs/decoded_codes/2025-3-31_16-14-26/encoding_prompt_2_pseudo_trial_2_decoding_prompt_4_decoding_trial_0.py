def doMain():
    # Prompt the user for the first set of values
    firstSet = input()
    # Prompt the user for the second set of values
    secondSet = input()
    
    # Split the input strings into lists of strings
    firstList = firstSet.split()
    secondList = secondSet.split()
    
    # Initialize the counter for differences
    differenceCount = 0
    
    # Loop through each index from 0 to 2 (inclusive)
    for i in range(3):
        # Convert the values to integers
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # If the values are not equal, increment the difference count
        if firstValue != secondValue:
            differenceCount += 1
    
    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
if __name__ == "__main__":
    doMain()
