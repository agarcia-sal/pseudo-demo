# Start of the program to compare two sets of three numbers
def compare_number_sets():
    # Step 2: Receive Input
    firstSet = input()
    secondSet = input()

    # Step 3: Split Input into Individual Numbers
    firstNumbers = firstSet.split()
    secondNumbers = secondSet.split()

    # Step 4: Initialize Difference Count
    differenceCount = 0

    # Step 5: Compare the Numbers
    for i in range(3):  # Loop through positions 0 to 2
        firstNumber = int(firstNumbers[i])  # Convert to integer
        secondNumber = int(secondNumbers[i])  # Convert to integer
        if firstNumber != secondNumber:  # Check for difference
            differenceCount += 1  # Increment difference count

    # Step 6: Evaluate Differences
    if differenceCount < 3:
        print("YES")  # Output if differences are less than 3
    else:
        print("NO")  # Output if differences are 3 or more

# Call the function to execute the program
compare_number_sets()
