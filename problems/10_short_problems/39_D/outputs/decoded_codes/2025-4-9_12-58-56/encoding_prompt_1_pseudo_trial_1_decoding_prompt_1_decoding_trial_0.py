def main():
    # Read input from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for different numbers
    differenceCount = 0

    # Loop through the number lists to compare each number
    for index in range(3):
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Check if the current numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1

    # Determine the output based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
