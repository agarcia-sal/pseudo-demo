def doMain():
    # Prompt the user to enter the first string of numbers
    firstInput = input()
    # Prompt the user to enter the second string of numbers
    secondInput = input()

    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Compare the first three numbers from both lists
    for index in range(3):
        firstNumber = int(firstList[index])  # Convert string to integer
        secondNumber = int(secondList[index])  # Convert string to integer
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment difference count if not equal

    # Check the count of differences to determine output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function to run the program
doMain()
