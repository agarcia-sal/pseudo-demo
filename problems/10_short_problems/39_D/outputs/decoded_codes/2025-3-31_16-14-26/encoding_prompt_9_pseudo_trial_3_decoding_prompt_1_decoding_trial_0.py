# Start Program Execution

def doMain():
    # Prompt the user for input and read two lines containing numeric values.
    firstSequence = input().split()
    secondSequence = input().split()
    
    # Initialize a variable called differenceCount to 0.
    differenceCount = 0

    # Compare Corresponding Values in the Two Sequences
    for index in range(3):
        # Convert values to integers
        firstValue = int(firstSequence[index])
        secondValue = int(secondSequence[index])

        # If the values are not equal, increment differenceCount
        if firstValue != secondValue:
            differenceCount += 1

    # Determine Output Based on Differences Count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute Main Function When the Program Starts
doMain()
