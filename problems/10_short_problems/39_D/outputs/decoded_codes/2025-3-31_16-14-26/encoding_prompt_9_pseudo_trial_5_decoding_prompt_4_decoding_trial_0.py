def doMain():
    # Receive First Input
    firstInput = input()
    # Receive Second Input
    secondInput = input()
    
    # Split Inputs into Lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a Counter for Differences
    differenceCount = 0

    # Loop through the Range from 0 to 2 (for three comparisons)
    for i in range(3):
        # Convert the elements at index i to integers
        valueFromFirst = int(firstList[i])
        valueFromSecond = int(secondList[i])
        
        # If the two values are not equal, increment the counter
        if valueFromFirst != valueFromSecond:
            differenceCount += 1

    # Check the Number of Differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the Function doMain when the Program Starts
doMain()
