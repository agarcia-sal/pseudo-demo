def main():
    # Prompt the user for input
    firstInput = input()
    secondInput = input()

    # Split the inputs into lists of numbers
    firstNumbers = firstInput.split()
    secondNumbers = secondInput.split()

    # Initialize a variable to count differences
    differenceCount = 0

    # Compare the numbers at each position
    for index in range(3):
        firstNumber = int(firstNumbers[index])
        secondNumber = int(secondNumbers[index])
        
        # If the numbers differ, increment the difference count
        if firstNumber != secondNumber:
            differenceCount += 1

    # Determine the result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
