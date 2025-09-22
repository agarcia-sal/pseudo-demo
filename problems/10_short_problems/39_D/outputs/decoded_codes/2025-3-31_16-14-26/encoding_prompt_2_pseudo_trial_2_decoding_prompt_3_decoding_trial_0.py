def doMain():
    # Prompt user for the first set of values and split into a list
    firstSet = input()
    firstList = firstSet.split()

    # Prompt user for the second set of values and split into a list
    secondSet = input()
    secondList = secondSet.split()

    # Initialize the counter for differences
    differenceCount = 0

    # Loop through each index from 0 to 2
    for index in range(3):
        # Convert values from both lists to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Increment differenceCount if values are not equal
        if firstValue != secondValue:
            differenceCount += 1

    # Output "YES" if there are less than 3 differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the doMain function when the program starts
doMain()
