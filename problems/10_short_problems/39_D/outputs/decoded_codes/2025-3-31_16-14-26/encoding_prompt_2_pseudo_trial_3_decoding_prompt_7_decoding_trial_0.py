def doMain():
    # Prompt user for the first set of values
    firstInput = input()
    # Prompt user for the second set of values
    secondInput = input()

    # Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Initialize a counter for differing values
    differenceCount = 0

    # Loop through the values for three iterations
    for i in range(3):
        # Convert the current values to integers
        firstValue = int(firstValues[i])
        secondValue = int(secondValues[i])

        # Compare the two values and count differences
        if firstValue != secondValue:
            differenceCount += 1

    # After the loop, check the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Check if the program is being executed as the main program
if __name__ == "__main__":
    doMain()
