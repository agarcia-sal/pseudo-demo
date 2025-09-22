def doMain():
    # Prompt the user to enter the first string of numbers
    firstInput = input()
    # Prompt the user to enter the second string of numbers
    secondInput = input()

    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for the differences
    differenceCount = 0

    # Iterate through the indices 0 to 2
    for index in range(3):
        # Convert the strings to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Count the number of differing numbers
        if firstNumber != secondNumber:
            differenceCount += 1

    # Check the count of differences to determine the output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the function to execute the program
doMain()
