def doMain():
    # Prompt the user for input
    firstSequence = input().split()  # Read first sequence of numbers
    secondSequence = input().split()  # Read second sequence of numbers

    # Initialize difference count
    differenceCount = 0

    # Compare corresponding values in the two sequences
    for index in range(3):
        # Convert values to integers
        firstValue = int(firstSequence[index])
        secondValue = int(secondSequence[index])
        
        # Check if values are different
        if firstValue != secondValue:
            differenceCount += 1  # Increment count of differences

    # Determine output based on differences count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute main function when the program starts
doMain()
