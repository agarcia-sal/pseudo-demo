def doMain():
    # Prompt the user for two strings of numbers
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for the differences
    differenceCount = 0

    # Iterate over the range to compare corresponding elements
    for index in range(3):
        # Convert the strings to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Increase the difference count if the numbers do not match
        if firstNumber != secondNumber:
            differenceCount += 1

    # Check the number of differences and output accordingly
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
doMain()
