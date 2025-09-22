def doMain():
    # Prompt the user for input for the first sequence and convert it to a list of strings
    firstSequence = input().split()
    # Prompt the user for input for the second sequence and convert it to a list of strings
    secondSequence = input().split()
    
    # Initialize the count of differences
    differenceCount = 0

    # Compare corresponding values in the two sequences
    for index in range(3):
        # Convert values to integers for comparison
        firstValue = int(firstSequence[index])
        secondValue = int(secondSequence[index])
        
        # If the values differ, increment the difference count
        if firstValue != secondValue:
            differenceCount += 1

    # Determine output based on the difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
doMain()
