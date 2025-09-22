def compare_number_sets():
    # Receive Input
    firstSet = input()
    secondSet = input()

    # Split Input into Individual Numbers
    firstList = firstSet.split()
    secondList = secondSet.split()

    # Initialize a Mismatch Counter
    mismatchCount = 0

    # Compare Corresponding Numbers
    for index in range(3):  # Iterate over indices 0 to 2
        firstNumber = int(firstList[index])  # Convert to integer
        secondNumber = int(secondList[index])  # Convert to integer
        if firstNumber != secondNumber:
            mismatchCount += 1  # Increment mismatch counter if numbers are not equal

    # Determine and Output the Result
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Program Execution
compare_number_sets()
