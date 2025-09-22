def doMain():
    # Step 1: Get input from the user
    firstInput = input()  # Take first input from the user
    secondInput = input()  # Take second input from the user

    # Step 2: Split the input strings into lists of numbers
    firstNumbers = firstInput.split()  # Split first input into a list of strings
    secondNumbers = secondInput.split()  # Split second input into a list of strings

    # Step 3: Initialize a counter for differences
    differenceCount = 0  # Initialize difference counter

    # Step 4: Compare corresponding elements of the two number lists
    for index in range(3):  # We assume there are exactly three elements to compare
        # Convert string to integer for comparison
        firstNumber = int(firstNumbers[index])  # Convert first number to integer
        secondNumber = int(secondNumbers[index])  # Convert second number to integer

        # Check if the numbers are different
        if firstNumber != secondNumber:  # Check if they are different
            differenceCount += 1  # Increment the difference count

    # Step 5: Output result based on the number of differences
    if differenceCount < 3:  # Check the count of differences
        print("YES")  # Print "YES" if less than 3 differences
    else:
        print("NO")  # Print "NO" if 3 or more differences

# Main execution starts here
doMain()  # Call the function to execute the program
