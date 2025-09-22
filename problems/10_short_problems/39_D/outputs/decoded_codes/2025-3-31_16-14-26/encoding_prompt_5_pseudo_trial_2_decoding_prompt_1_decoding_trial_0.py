def main():
    # Accept input for the first set of values
    firstSet = input()

    # Accept input for the second set of values
    secondSet = input()

    # Split the input strings into lists of individual numbers
    firstValues = firstSet.split()
    secondValues = secondSet.split()

    # Initialize a counter for the number of differences
    differenceCount = 0 

    # Loop through each position to compare the values
    for index in range(3):
        # Convert the current values from string to integer
        valueFromFirstSet = int(firstValues[index])
        valueFromSecondSet = int(secondValues[index])

        # Check if the values at the current index are different
        if valueFromFirstSet != valueFromSecondSet:
            # Increase the difference counter by one
            differenceCount += 1 

    # Determine if the number of differences is less than three
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
