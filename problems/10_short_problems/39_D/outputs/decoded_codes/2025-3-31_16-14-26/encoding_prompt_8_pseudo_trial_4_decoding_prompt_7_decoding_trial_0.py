def mainProcedure():
    # Step 1: Accept two lines of input
    firstInput = input()  # Read first set of numbers from user
    secondInput = input()  # Read second set of numbers from user

    # Step 2: Split the input strings into lists of numbers
    firstList = firstInput.split()  # Split first input into strings
    secondList = secondInput.split()  # Split second input into strings

    # Step 3: Initialize a counter to track differences
    differenceCount = 0 

    # Step 4: Compare the numbers in both lists
    for index in range(3):  # Loop through the first three indices
        # Convert current elements to integers for comparison
        firstNumber = int(firstList[index])  # Convert to integer
        secondNumber = int(secondList[index])  # Convert to integer

        # Check if the numbers are not equal
        if firstNumber != secondNumber:  # Compare the numbers
            # Increment the difference counter
            differenceCount += 1 

    # Step 5: Determine the outcome based on the number of differences
    if differenceCount < 3:  # Check if differences are less than 3
        print("YES")  # Output YES if conditions are met
    else:
        print("NO")  # Output NO if conditions are not met

# Execute the main procedure when the program runs
mainProcedure()
