def CompareTwoSetsOfNumbers():
    # Step 1: Get user input for two sets of numbers
    firstSet = input()
    secondSet = input()

    # Step 2: Split each set of numbers into individual elements
    firstList = firstSet.split()
    secondList = secondSet.split()

    # Step 3: Initialize a counter to track differences
    differenceCount = 0

    # Step 4: Compare corresponding numbers in both sets
    for index in range(3):
        # Convert string to integer for comparison
        numberFromFirstSet = int(firstList[index])
        numberFromSecondSet = int(secondList[index])

        # Step 5: Check if the numbers are different
        if numberFromFirstSet != numberFromSecondSet:
            differenceCount += 1 

    # Step 6: Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")  # The sets are sufficiently similar
    else:
        print("NO")   # The sets are too different

# Main execution 
CompareTwoSetsOfNumbers()
