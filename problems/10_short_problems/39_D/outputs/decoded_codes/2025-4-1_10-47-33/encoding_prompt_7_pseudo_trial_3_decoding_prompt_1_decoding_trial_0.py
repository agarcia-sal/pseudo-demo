def main():
    # Read input for two sets of numbers
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Compare the first three numbers in both lists
    for index in range(3):
        # Convert the current elements to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])

        # Check if the numbers are different
        if firstNumber != secondNumber:
            # Increment the differences counter
            differenceCount += 1

    # Determine output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point for the program
if __name__ == "__main__":
    main()
