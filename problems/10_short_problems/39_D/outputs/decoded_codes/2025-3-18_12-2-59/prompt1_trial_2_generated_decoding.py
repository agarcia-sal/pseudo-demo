def doMain():
    # Read two lines of input from the user
    firstLine = input()
    secondLine = input()

    # Split the input lines into lists of strings
    firstValues = firstLine.split()
    secondValues = secondLine.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string values to integers
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])

        # Check for equality
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1

    # Check how many differences were counted
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
doMain()
