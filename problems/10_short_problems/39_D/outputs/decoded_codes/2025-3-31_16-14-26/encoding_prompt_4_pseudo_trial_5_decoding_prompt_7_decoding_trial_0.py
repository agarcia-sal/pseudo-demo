def doMain():
    # Read two lines of input from the user
    firstLine = input()
    secondLine = input()

    # Split the input lines into lists of strings
    firstList = firstLine.split()
    secondList = secondLine.split()

    # Initialize a counter for the differences
    differenceCount = 0

    # Loop through the first 3 elements of both lists
    for index in range(3):
        # Convert string elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Compare the two values
        if firstValue != secondValue:
            # Increment the difference count if they are not the same
            differenceCount += 1

    # Check the number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    doMain()
