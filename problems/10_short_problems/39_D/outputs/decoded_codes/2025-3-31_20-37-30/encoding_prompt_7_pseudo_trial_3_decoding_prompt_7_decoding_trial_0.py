def doMain():
    # Get user input for two sets of three values
    firstInput = input()
    secondInput = input()

    # Split the inputs into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Initialize the mismatch counter
    mismatchCount = 0 

    # Compare the corresponding values from both lists
    for index in range(3):  # Loop over indices 0 to 2
        # Convert the values to integers for comparison
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])

        # Check if the values do not match
        if firstValue != secondValue:
            # Increment the mismatch counter
            mismatchCount += 1 

    # Determine if the number of mismatches is less than 3
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    doMain()
