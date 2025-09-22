def compareInputs():
    # Get the first set of three numbers from the user
    print("Enter the first set of numbers:")
    firstInput = input()  # User input for the first set
    
    # Get the second set of three numbers from the user
    print("Enter the second set of numbers:")
    secondInput = input()  # User input for the second set

    # Split the input strings into lists of numbers
    firstSet = firstInput.split()  # Split the first input into a list
    secondSet = secondInput.split()  # Split the second input into a list

    # Initialize a counter for differences
    differenceCount = 0  # Counter for the number of different positions

    # Loop through each position of the sets (0 to 2)
    for index in range(3):  # Iterate over the range of 3
        # Convert the numbers at the current index to integers
        firstNumber = int(firstSet[index])  # Convert the first number to integer
        secondNumber = int(secondSet[index])  # Convert the second number to integer

        # If the numbers are different, increment the difference counter
        if firstNumber != secondNumber:  # Check if the numbers are not equal
            differenceCount += 1  # Increment the difference count

    # If the number of differences is less than 3, print "YES"
    if differenceCount < 3:  # Check if differences are fewer than 3
        print("YES")  # Output for fewer than 3 differences
    else:
        # Otherwise, print "NO"
        print("NO")  # Output when there are 3 or more differences

# Start the program
compareInputs()  # Call the function to execute the comparison
