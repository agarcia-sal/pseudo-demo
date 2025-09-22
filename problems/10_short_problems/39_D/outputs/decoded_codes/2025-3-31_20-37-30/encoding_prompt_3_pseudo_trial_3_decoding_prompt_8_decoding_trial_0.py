def main():
    # Step 1: Read input values
    firstInput = input()
    secondInput = input()

    # Step 2: Split inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 3: Initialize a counter for non-matching elements
    mismatchCount = 0

    # Step 4: Compare elements in the lists
    for index in range(3):  # Assuming both lists have at least 3 elements
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Step 5: Check for discrepancies
        if firstValue != secondValue:
            mismatchCount += 1

    # Step 6: Output result based on the count of mismatches
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute main function
main()
