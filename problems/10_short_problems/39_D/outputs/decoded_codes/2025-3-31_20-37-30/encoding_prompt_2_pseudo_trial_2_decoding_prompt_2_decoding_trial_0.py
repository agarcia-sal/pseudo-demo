def doMain():
    # Step 3: Get user input
    firstInput = input()
    secondInput = input()

    # Step 4: Split the inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 5: Initialize a counter
    differenceCount = 0

    # Step 6: Compare corresponding elements from the two lists
    for i in range(3):  # Looping through indices 0 to 2
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        if firstValue != secondValue:
            differenceCount += 1

    # Step 7: Determine the result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute the main function if the program is run as the main module
if __name__ == "__main__":
    doMain()
