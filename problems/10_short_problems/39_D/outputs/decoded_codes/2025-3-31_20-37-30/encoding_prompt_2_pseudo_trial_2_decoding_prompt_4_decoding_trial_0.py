def doMain():
    # Step 3: Get user input
    firstInput = input()
    secondInput = input()
    
    # Step 4: Split the inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Step 5: Initialize a counter for differences
    differenceCount = 0
    
    # Step 6: Compare corresponding elements from both lists
    for index in range(3):  # Looping through indices 0 to 2
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        
        if firstValue != secondValue:  # Check for difference
            differenceCount += 1  # Increment count of differences

    # Step 7: Determine the result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute the main function
if __name__ == "__main__":
    doMain()

# Step 9: End of program
