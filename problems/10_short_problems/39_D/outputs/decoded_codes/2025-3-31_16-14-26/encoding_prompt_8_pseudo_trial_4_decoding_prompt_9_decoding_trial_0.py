def mainProcedure():
    # Step 1: Accept two lines of input
    firstInput = input()
    secondInput = input()

    # Step 2: Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 3: Initialize a counter to track differences
    differenceCount = 0 

    # Step 4: Compare the numbers in both lists
    for index in range(3):  # iterate from 0 to 2
        # Convert current elements to integers for comparison
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])

        # Check if the numbers are not equal
        if firstNumber != secondNumber:
            # Increment the difference counter
            differenceCount += 1 

    # Step 5: Determine the outcome based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main procedure when the program runs
mainProcedure()
