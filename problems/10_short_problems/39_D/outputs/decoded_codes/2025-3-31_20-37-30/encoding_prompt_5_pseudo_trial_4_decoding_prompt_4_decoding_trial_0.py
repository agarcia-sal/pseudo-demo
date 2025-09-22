def doMain():
    # Accept input from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Initialize the counter for differences
    differenceCount = 0

    # Compare the values in both lists
    for index in range(3):
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # If values differ, increment the counter
        if firstValue != secondValue:
            differenceCount += 1

    # Output result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is being run as the main program
if __name__ == "__main__":
    doMain()
