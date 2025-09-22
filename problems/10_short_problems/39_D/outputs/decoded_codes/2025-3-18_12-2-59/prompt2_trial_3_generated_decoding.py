def doMain():
    # Step 3: Prompt for the first string of numbers
    firstInput = input()
    
    # Step 4: Prompt for the second string of numbers
    secondInput = input()
    
    # Step 5: Split firstInput into a list of strings
    firstList = firstInput.split()
    
    # Step 6: Split secondInput into a list of strings
    secondList = secondInput.split()
    
    # Step 7: Initialize differenceCount
    differenceCount = 0

    # Step 8: Loop through the first three elements (indices 0 to 2)
    for index in range(3):
        firstNumber = int(firstList[index])  # Convert to integer
        secondNumber = int(secondList[index])  # Convert to integer
        
        # Check for difference
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment if they differ

    # Step 9: Check the value of differenceCount
    if differenceCount < 3:
        print("YES")  # Output if fewer than 3 differences
    else:
        print("NO")   # Output if 3 or more differences

# Step 11: Check if the script is being run as the main program
if __name__ == "__main__":
    doMain()  # Call the function
