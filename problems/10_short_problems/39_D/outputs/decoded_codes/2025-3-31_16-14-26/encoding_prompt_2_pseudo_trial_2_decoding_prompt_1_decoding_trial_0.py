# Start the program.

def doMain():
    # Prompt the user to enter the first set of values and store the input as firstSet.
    firstSet = input()
    # Prompt the user to enter the second set of values and store the input as secondSet.
    secondSet = input()
    # Split firstSet into a list of values called firstList.
    firstList = firstSet.split()
    # Split secondSet into a list of values called secondList.
    secondList = secondSet.split()
    # Initialize a counter called differenceCount to zero.
    differenceCount = 0
    
    # Loop through each index from 0 to 2:
    for i in range(3):
        # Convert the value at the current index in firstList to an integer and store it as firstValue.
        firstValue = int(firstList[i])
        # Convert the value at the current index in secondList to an integer and store it as secondValue.
        secondValue = int(secondList[i])
        # If firstValue is not equal to secondValue:
        if firstValue != secondValue:
            # Increment the differenceCount by one.
            differenceCount += 1
    
    # After the loop:
    # If differenceCount is less than 3:
    if differenceCount < 3:
        # Output "YES".
        print("YES")
    # Otherwise:
    else:
        # Output "NO".
        print("NO")

# Execute the doMain function when the program starts.
doMain()

# End the program.
