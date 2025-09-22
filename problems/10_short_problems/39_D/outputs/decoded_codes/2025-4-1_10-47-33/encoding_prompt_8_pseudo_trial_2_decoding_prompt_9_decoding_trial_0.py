def compareThreeIntegers():
    # Prompt the user for input and store as firstInput
    firstInput = input()
    # Prompt the user for input and store as secondInput
    secondInput = input()

    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize difference counter
    differenceCount = 0

    # Comparison loop for each index from 0 to 2
    for index in range(3):
        # Convert the items to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Check if the values differ
        if firstValue != secondValue:
            # Increment the difference count if they are not equal
            differenceCount += 1

    # Check if the difference count is less than 3
    if differenceCount < 3:
        print("YES")  # Output "YES" if they differ by less than 3
    else:
        print("NO")   # Output "NO" otherwise

# Call the function to execute the program
compareThreeIntegers()
