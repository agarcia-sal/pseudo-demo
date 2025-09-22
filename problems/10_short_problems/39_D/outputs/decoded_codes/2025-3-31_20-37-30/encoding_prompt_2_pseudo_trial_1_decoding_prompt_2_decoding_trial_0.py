def doMain():
    # Step 2: Read two strings from user input
    firstInput = input()
    secondInput = input()

    # Step 3: Split the firstInput into a list of strings
    firstList = firstInput.split()
    # Step 4: Split the secondInput into a list of strings
    secondList = secondInput.split()

    # Step 5: Initialize a variable for counting differences
    differencesCount = 0

    # Step 6: Loop over the indices from 0 to 2
    for index in range(3):
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        
        # Check for differences
        if firstValue != secondValue:
            differencesCount += 1  # Increment if not equal

    # Step 7: Check the number of differences
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Call the doMain function if script is executed directly
if __name__ == "__main__":
    doMain()
