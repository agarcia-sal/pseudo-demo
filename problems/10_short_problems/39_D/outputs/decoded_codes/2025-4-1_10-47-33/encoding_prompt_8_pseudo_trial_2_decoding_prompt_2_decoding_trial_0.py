def compareThreeIntegers():
    # Input handling
    firstInput = input()  # Prompt for the first line of integers
    secondInput = input()  # Prompt for the second line of integers

    # Data processing
    firstList = firstInput.split()  # Split the first input into a list of strings
    secondList = secondInput.split()  # Split the second input into a list of strings

    # Initialize difference counter
    differenceCount = 0  # Counter for differences

    # Comparison loop
    for index in range(3):  # Loop through indices 0, 1, 2
        firstValue = int(firstList[index])  # Convert firstList value to integer
        secondValue = int(secondList[index])  # Convert secondList value to integer

        # Check for difference
        if firstValue != secondValue:  # If values are not equal
            differenceCount += 1  # Increment the difference counter

    # Condition check
    if differenceCount < 3:  # If the difference count is less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Execution
compareThreeIntegers()  # Call the function
