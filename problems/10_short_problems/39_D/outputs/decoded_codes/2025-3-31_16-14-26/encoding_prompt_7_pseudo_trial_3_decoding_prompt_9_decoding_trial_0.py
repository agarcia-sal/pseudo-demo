def doMain():
    # Read two lines of input
    firstLine = input()
    secondLine = input()

    # Split the input strings into lists of strings
    firstList = firstLine.split()
    secondList = secondLine.split()

    # Initialize a variable to count the number of differences
    differenceCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from strings to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # If the values are not equal, increment the difference counter
        if firstValue != secondValue:
            differenceCount += 1

    # If the number of differences is less than 3, print "YES"
    if differenceCount < 3:
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Execute the main function when this script is run directly
if __name__ == "__main__":
    doMain()
