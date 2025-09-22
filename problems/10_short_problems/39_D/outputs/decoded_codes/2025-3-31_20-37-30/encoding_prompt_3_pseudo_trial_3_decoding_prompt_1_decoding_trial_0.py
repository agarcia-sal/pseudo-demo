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
    for index in range(3):
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer

        # Step 5: Check for discrepancies
        if firstValue != secondValue:  # Check if not equal
            mismatchCount += 1  # Increment mismatch count

    # Step 6: Output result based on the count of mismatches
    if mismatchCount < 3:  # If less than 3 mismatches
        print("YES")
    else:
        print("NO")

# Step 7: Execute main function
main()
