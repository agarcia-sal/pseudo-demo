def doMain():
    # Prompt the user to enter the first set of values
    firstSet = input()
    # Prompt the user to enter the second set of values
    secondSet = input()
    
    # Split the input strings into lists of values
    firstList = firstSet.split()
    secondList = secondSet.split()
    
    # Initialize a counter for the differences
    differenceCount = 0
    
    # Loop through each index from 0 to 2
    for index in range(3):
        # Convert the values at the current index to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # If the values are not equal, increment the difference count
        if firstValue != secondValue:
            differenceCount += 1
    
    # After the loop, check the difference count
    if differenceCount < 3:
        print("YES")  # Output YES if fewer than three differences
    else:
        print("NO")   # Output NO if three or more differences

# Execute the doMain function when the program starts
doMain()
