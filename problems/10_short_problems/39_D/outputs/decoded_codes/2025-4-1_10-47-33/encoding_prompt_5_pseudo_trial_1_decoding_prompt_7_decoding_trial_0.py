def main():
    # Prompt the user for input
    firstInput = input()  # Getting the first line of input
    secondInput = input()  # Getting the second line of input

    # Split the inputs into lists of numbers
    firstNumbers = firstInput.split()  # Splitting by spaces into a list
    secondNumbers = secondInput.split()  # Splitting by spaces into a list

    # Initialize a variable to count differences
    differenceCount = 0  # Start with zero differences

    # Compare the numbers at each position
    for index in range(3):  # Loop through the first three indices (0 to 2)
        firstNumber = int(firstNumbers[index])  # Convert to integer
        secondNumber = int(secondNumbers[index])  # Convert to integer
        
        # If the numbers differ, increment the difference count
        if firstNumber != secondNumber:  # Check for inequality
            differenceCount += 1  # Increment the difference count

    # Determine the result based on the number of differences
    if differenceCount < 3:  # If less than three differences
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Start the program
main()  # Call the main function to execute
