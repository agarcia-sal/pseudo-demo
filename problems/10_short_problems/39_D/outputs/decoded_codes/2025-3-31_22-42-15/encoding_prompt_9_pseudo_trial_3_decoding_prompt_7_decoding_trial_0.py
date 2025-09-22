def main():
    # Get two input strings representing numerical values
    firstSet = input()
    secondSet = input()

    # Split the input strings into lists of numerical strings
    numbersFromFirstSet = firstSet.split()
    numbersFromSecondSet = secondSet.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Loop through the range of three positions
    for position in range(3):  # We expect exactly three values in each set
        # Convert the current positions' values from strings to integers
        valueFromFirstSet = int(numbersFromFirstSet[position])
        valueFromSecondSet = int(numbersFromSecondSet[position])

        # Check if the values from both sets differ
        if valueFromFirstSet != valueFromSecondSet:
            # Increment the difference counter
            differenceCount += 1

    # Check the total differences and decide the output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()
