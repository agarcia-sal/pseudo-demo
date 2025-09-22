def main():
    # Step 1: Read input values
    firstInput = input()  # Get first user input
    secondInput = input()  # Get second user input

    # Step 2: Split inputs into lists of strings
    firstList = firstInput.split()  # Split first input into list
    secondList = secondInput.split()  # Split second input into list

    # Step 3: Initialize a counter for non-matching elements
    mismatchCount = 0  # Counter for discrepancies

    # Step 4: Compare elements in the lists
    for index in range(3):  # Loop through first three elements
        # Convert elements to integers for comparison
        firstValue = int(firstList[index])  
        secondValue = int(secondList[index])  

        # Step 5: Check for discrepancies
        if firstValue != secondValue:  # If values differ
            mismatchCount += 1  # Increment mismatch counter

    # Step 6: Output result based on the count of mismatches
    if mismatchCount < 3:  # If mismatches are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Step 7: Execute main function
main()
