# Start Program Execution

def doMain():
    # Prompt user for input and read two lines containing numeric values
    firstSequence = input().split()  # Read first sequence of numbers
    secondSequence = input().split()  # Read second sequence of numbers
    
    # Initialize a variable to count the differences
    differenceCount = 0

    # Compare corresponding values in the two sequences
    for index in range(3):  # Loop through indices 0 to 2
        firstValue = int(firstSequence[index])  # Convert the first sequence value to int
        secondValue = int(secondSequence[index])  # Convert the second sequence value to int
        
        # If the values are not equal, increment the difference count
        if firstValue != secondValue:
            differenceCount += 1

    # Determine output based on difference count
    if differenceCount < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" otherwise

# Execute main function when the program starts
doMain()
