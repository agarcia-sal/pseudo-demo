def doMain():
    # Read two lines of input
    firstLine = input()
    secondLine = input()

    # Split input lines into lists of strings
    list1 = firstLine.split()
    list2 = secondLine.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        valueA = int(list1[index])
        valueB = int(list2[index])

        # Check if the two values are different
        if valueA != valueB:
            differenceCount += 1

    # Check the number of differences
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences


# Main program execution
if __name__ == "__main__":
    doMain()
