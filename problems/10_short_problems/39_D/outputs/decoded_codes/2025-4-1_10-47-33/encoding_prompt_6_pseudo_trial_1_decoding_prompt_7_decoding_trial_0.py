def main():
    # Read two lines of input from the user
    firstLine = input()
    secondLine = input()

    # Split the input lines into lists of strings
    firstList = firstLine.split(" ")
    secondList = secondLine.split(" ")

    # Initialize a variable to count the number of differences
    differenceCount = 0

    # Loop through the first three elements of the lists
    for index in range(3):  # Loop from 0 to 2 inclusive
        # Convert the string values at the current index to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Check if the values from both lists are different
        if firstValue != secondValue:
            # If they are different, increment the difference count
            differenceCount += 1

    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
