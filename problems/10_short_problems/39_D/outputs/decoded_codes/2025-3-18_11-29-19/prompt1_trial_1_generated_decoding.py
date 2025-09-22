def main():
    # Read two lines of input from the user
    firstLine = input()
    secondLine = input()

    # Split the input strings into lists of substrings
    firstList = firstLine.split()
    secondList = secondLine.split()

    # Initialize a counter to track differences
    differenceCount = 0

    # Loop through the first three elements of the lists
    for index in range(3):  # index goes from 0 to 2
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Check if the values are different
        if firstValue != secondValue:
            # Increase the difference count
            differenceCount += 1

    # Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
