def doMain():
    # Prompt user for the first set of values and split into a list
    firstInput = input()
    firstValues = firstInput.split()

    # Prompt user for the second set of values and split into a list
    secondInput = input()
    secondValues = secondInput.split()

    # Initialize a counter for the number of differing values
    differenceCount = 0

    # Loop to compare the values at the same indexes
    for i in range(3):
        # Convert string values to integers
        firstValue = int(firstValues[i])
        secondValue = int(secondValues[i])

        # Compare the integer values and increment the count if they differ
        if firstValue != secondValue:
            differenceCount += 1

    # Output result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# If the program is executed as the main program, run the doMain function
if __name__ == "__main__":
    doMain()
