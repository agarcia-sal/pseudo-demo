def main():
    firstInput = readInput()      # Get the first set of integers
    secondInput = readInput()     # Get the second set of integers

    differenceCount = 0

    for index in range(3):
        firstNumber = convertToInteger(firstInput[index])   # Convert to integer
        secondNumber = convertToInteger(secondInput[index]) # Convert to integer

        if firstNumber != secondNumber:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")


def readInput():
    inputLine = input()          # Read a line from user input
    return inputLine.split()     # Split the line into separate strings


def convertToInteger(stringValue):
    return int(stringValue)      # Convert and return the integer representation of the string

# Call the main function to execute the program
if __name__ == "__main__":
    main()
