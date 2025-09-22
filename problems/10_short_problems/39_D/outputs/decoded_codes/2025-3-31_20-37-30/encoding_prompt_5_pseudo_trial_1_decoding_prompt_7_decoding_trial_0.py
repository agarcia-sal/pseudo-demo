def CompareTwoSetsOfNumbers():
    # Step 1: Get user input for two sets of numbers
    firstSet = input()  # Input first set of numbers
    secondSet = input()  # Input second set of numbers

    # Step 2: Split each set of numbers into individual elements
    firstList = firstSet.split()  # Split first set into list
    secondList = secondSet.split()  # Split second set into list

    # Step 3: Initialize a counter to track differences
    differenceCount = 0 

    # Step 4: Compare corresponding numbers in both sets
    for index in range(3):  # Loop through 0 to 2
        # Convert string to integer for comparison
        numberFromFirstSet = int(firstList[index])  # Convert from first list
        numberFromSecondSet = int(secondList[index])  # Convert from second list

        # Step 5: Check if the numbers are different
        if numberFromFirstSet != numberFromSecondSet: 
            differenceCount += 1  # Increment counter if numbers differ

    # Step 6: Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")  # The sets are sufficiently similar
    else:
        print("NO")  # The sets are too different

# Main execution 
CompareTwoSetsOfNumbers()
