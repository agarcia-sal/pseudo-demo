def doMain():
    # Step 2: Read two strings from user input
    firstInput = input()
    secondInput = input()

    # Step 3: Split the firstInput into a list of strings
    firstList = firstInput.split()
    # Step 4: Split the secondInput into a list of strings
    secondList = secondInput.split()

    # Step 5: Initialize differencesCount to zero
    differencesCount = 0

    # Step 6: Check the first three pairs of values
    for index in range(3):  # Loop from 0 to 2
        # Convert the values at the current index to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # If values are not equal, increment the differencesCount
        if firstValue != secondValue:
            differencesCount += 1

    # Step 7: Determine the output based on differencesCount
    if differencesCount < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")   # Output "NO" otherwise

# Step 8: Check if the script is executed directly
if __name__ == "__main__":
    doMain()  # Call the doMain function to execute the program
