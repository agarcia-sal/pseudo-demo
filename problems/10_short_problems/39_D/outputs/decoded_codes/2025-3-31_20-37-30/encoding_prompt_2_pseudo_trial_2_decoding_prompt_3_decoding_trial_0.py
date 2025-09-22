def doMain():
    # Get user input
    firstInput = input()
    secondInput = input()

    # Split the inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Compare corresponding elements from both lists
    for i in range(3):  # We will only check the first three elements
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        if firstValue != secondValue:
            differenceCount += 1

    # Determine the result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the program is run as the main module
if __name__ == "__main__":
    doMain()
