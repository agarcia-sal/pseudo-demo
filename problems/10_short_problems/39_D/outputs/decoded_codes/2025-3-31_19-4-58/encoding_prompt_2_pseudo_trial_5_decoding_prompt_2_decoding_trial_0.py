# Start the program
def doMain():
    # Prompt the user to enter the first string of numbers
    firstInput = input()
    # Prompt the user to enter the second string of numbers
    secondInput = input()

    # Split the firstInput string into a list of strings
    firstList = firstInput.split()
    # Split the secondInput string into a list of strings
    secondList = secondInput.split()

    # Initialize a counter variable named differenceCount
    differenceCount = 0

    # For each index from 0 to 2 do the following:
    for index in range(3):
        # Convert the string at current index of firstList to an integer
        firstNumber = int(firstList[index])
        # Convert the string at current index of secondList to an integer
        secondNumber = int(secondList[index])

        # If firstNumber is not equal to secondNumber:
        if firstNumber != secondNumber:
            # Increase the differenceCount by 1
            differenceCount += 1

    # If differenceCount is less than 3:
    if differenceCount < 3:
        # Output "YES"
        print("YES")
    else:
        # Otherwise: Output "NO"
        print("NO")

# Invoke the function doMain to execute the program
doMain()
