def doMain():
    # Receive first input
    firstInput = input()
    
    # Receive second input
    secondInput = input()
    
    # Split inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0

    # Loop through the range from 0 to 2 (for three comparisons)
    for i in range(3):
        # Convert elements at index i to integers
        valueFromFirst = int(firstList[i])
        valueFromSecond = int(secondList[i])
        
        # If the two values are not equal
        if valueFromFirst != valueFromSecond:
            differenceCount += 1  # Increment the difference count

    # Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the function doMain when the program starts
doMain()
