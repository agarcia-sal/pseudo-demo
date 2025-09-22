def doMain():
    # Get user input
    firstInput = input()
    secondInput = input()

    # Split the inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Compare corresponding elements from the two lists
    for index in range(3):  # Loop through the first three indices (0 to 2)
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        if firstValue != secondValue:  # Check if the values differ
            differenceCount += 1  # Increment the count of differences

    # Determine the result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the program is run as the main module
if __name__ == "__main__":
    doMain()
