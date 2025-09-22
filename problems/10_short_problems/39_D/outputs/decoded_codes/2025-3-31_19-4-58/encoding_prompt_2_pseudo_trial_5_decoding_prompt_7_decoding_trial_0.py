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

    # Iterate over the indices 0 to 2
    for index in range(3):
        # Convert the corresponding string values to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])

        # Check if the numbers are different
        if firstNumber != secondNumber:
            # Increase the difference count
            differenceCount += 1

    # Check the difference count against the threshold
    if differenceCount < 3:
        # If less than 3 differences, output "YES"
        print("YES")
    else:
        # Otherwise, output "NO"
        print("NO")

# Invoke the main function to execute the program
doMain()
