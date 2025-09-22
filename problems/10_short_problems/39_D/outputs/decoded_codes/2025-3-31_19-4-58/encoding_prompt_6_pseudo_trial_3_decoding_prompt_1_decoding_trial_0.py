def doMain():
    # Read inputs from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Compare the two values
        if firstValue != secondValue:
            # Increment the difference counter if the values are different
            differenceCount += 1

    # Decide the final output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
doMain()
