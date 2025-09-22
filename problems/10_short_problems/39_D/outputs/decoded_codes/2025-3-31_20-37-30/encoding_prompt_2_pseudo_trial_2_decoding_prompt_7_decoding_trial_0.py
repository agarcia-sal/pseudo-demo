def doMain():
    # Step 3: Get user input
    firstInput = input()  # Read the first input line
    secondInput = input()  # Read the second input line

    # Step 4: Split the inputs into lists
    firstList = firstInput.split()  # Split by spaces into a list
    secondList = secondInput.split()  # Split by spaces into a list

    # Step 5: Initialize a counter for differences
    differenceCount = 0  # This will track the number of differing elements

    # Step 6: Compare corresponding elements from the two lists
    # We're only checking the first three elements
    for index in range(3):  # Loop through indices 0, 1, 2
        firstValue = int(firstList[index])  # Convert element to integer from firstList
        secondValue = int(secondList[index])  # Convert element to integer from secondList

        # Check if the two values are different
        if firstValue != secondValue:
            differenceCount += 1  # Increment count if values differ

    # Step 7: Determine the result based on the count of differences
    if differenceCount < 3:
        print("YES")  # Print "YES" if differences are fewer than 3
    else:
        print("NO")  # Print "NO" if differences are 3 or more

# Step 8: Execute the main function if the program is run as the main module
if __name__ == "__main__":
    doMain()
