def main():
    # Read input from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of values
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter to track differences
    differenceCount = 0

    # Loop through the first three values of both lists
    for index in range(3):
        # Convert string values to integers
        valueFromFirstList = int(firstList[index])
        valueFromSecondList = int(secondList[index])

        # Check if the values are different
        if valueFromFirstList != valueFromSecondList:
            # Increment the difference counter
            differenceCount += 1

    # Check the number of differences and output the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
main()
