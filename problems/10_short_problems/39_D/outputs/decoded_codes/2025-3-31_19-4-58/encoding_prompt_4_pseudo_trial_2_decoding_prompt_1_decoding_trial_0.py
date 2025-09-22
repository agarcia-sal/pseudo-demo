def doMain():
    # Read inputs for two sets of three integers
    firstInput = input()
    secondInput = input()

    # Split inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for mismatches
    mismatchCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the corresponding values are different
        if firstValue != secondValue:
            # Increment the mismatch count
            mismatchCount += 1

    # Determine if the number of mismatches is less than 3
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution
doMain()
