def doMain():
    # Prompt the user to enter the first string of numbers
    firstInput = input()
    # Prompt the user to enter the second string of numbers
    secondInput = input()

    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Loop through indices 0 to 2
    for index in range(3):
        # Convert strings to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1

    # Output results based on the difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function to execute the program
doMain()
