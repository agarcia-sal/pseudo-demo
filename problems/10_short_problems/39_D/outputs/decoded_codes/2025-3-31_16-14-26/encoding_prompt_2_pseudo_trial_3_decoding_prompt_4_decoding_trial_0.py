def doMain():
    # Prompt user for the first set of values
    firstInput = input()
    # Prompt user for the second set of values
    secondInput = input()

    # Split the inputs into lists of strings
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Initialize the counter for differences
    differenceCount = 0

    # Iterate through the values for comparison
    for i in range(3):  # Loop through indices 0 to 2
        # Convert string values to integers
        firstValue = int(firstValues[i])
        secondValue = int(secondValues[i])
        
        # Compare the two values
        if firstValue != secondValue:
            differenceCount += 1  # Increment count if they differ

    # Output the result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    doMain()
