def doMain():
    # Prompt the user to enter the first set of values
    firstSet = input()
    # Prompt the user to enter the second set of values
    secondSet = input()
    
    # Split the entered sets into lists
    firstList = firstSet.split()
    secondList = secondSet.split()
    
    # Initialize a counter to count the differences
    differenceCount = 0
    
    # Loop through each index from 0 to 2
    for i in range(3):
        # Convert the values at the current index to integers
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1  # Increment the difference count if they do not match

    # After the loop, check how many differences were counted
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Execute the function when the program starts
doMain()
