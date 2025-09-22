def doMain():
    # Step 1: Get input from the user
    firstInput = input()
    secondInput = input()

    # Step 2: Split the input strings into lists of numbers
    firstNumbers = firstInput.split()
    secondNumbers = secondInput.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0 

    # Step 4: Compare corresponding elements of the two number lists
    for index in range(3):  # Loop from 0 to 2
        # Convert string to integer for comparison
        firstNumber = int(firstNumbers[index])
        secondNumber = int(secondNumbers[index])

        # Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment difference count by 1 

    # Step 5: Output result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
