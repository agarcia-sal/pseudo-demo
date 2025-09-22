def doMain():
    # Read input values from the user
    firstInput = input()
    secondInput = input()

    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a variable to count differences
    differenceCount = 0

    # Compare corresponding elements of the two lists
    for index in range(3):  # Assuming the input lists will always have at least 3 elements
        # Convert the string values to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Count differences
        if firstValue != secondValue:
            differenceCount += 1

    # Output the result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    doMain()
