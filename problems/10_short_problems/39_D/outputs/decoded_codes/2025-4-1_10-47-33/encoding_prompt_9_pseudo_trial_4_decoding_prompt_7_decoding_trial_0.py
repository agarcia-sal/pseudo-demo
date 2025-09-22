def main():
    # Receive input from the user
    firstInput = input()  # First line of input
    secondInput = input()  # Second line of input

    # Split the input strings into lists of strings
    firstList = firstInput.split()  # Splits first input by spaces into a list
    secondList = secondInput.split()  # Splits second input by spaces into a list

    # Initialize a counter to track position differences
    differenceCount = 0  # To count the differences between the two lists

    # Loop through the first three elements of both lists
    for index in range(3):  # Only iterate for 0, 1, and 2
        # Convert each string in the lists to an integer for comparison
        firstNumber = int(firstList[index])  # Convert to integer from first list
        secondNumber = int(secondList[index])  # Convert to integer from second list

        # If the numbers are not equal, increment the difference counter
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment the difference count by 1

    # Check if the difference count is less than 3
    if differenceCount < 3:
        print("YES")  # Output YES if differences are less than 3
    else:
        print("NO")  # Output NO otherwise

# Start the program execution
main()
