def doMain():
    # Read two lines of input
    firstSequence = input().split()
    secondSequence = input().split()
    
    # Initialize the difference count
    differenceCount = 0
    
    # Compare corresponding values in the two sequences
    for index in range(3):
        firstValue = int(firstSequence[index])
        secondValue = int(secondSequence[index])
        
        if firstValue != secondValue:
            differenceCount += 1
    
    # Determine output based on differences count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute main function when the program starts
doMain()
