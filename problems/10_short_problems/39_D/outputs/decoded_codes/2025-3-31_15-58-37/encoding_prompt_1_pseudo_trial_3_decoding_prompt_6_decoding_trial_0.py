def doMain():
    # Step 2: Read values from input
    firstInput = input()  # Read the first line of input
    secondInput = input()  # Read the second line of input
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Step 3: Initialize difference counter
    differenceCount = 0  # Count of differences
    
    # Step 4: Loop through the indices and check values
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        valueA = int(firstList[index])  # Convert the first list's value to integer
        valueB = int(secondList[index])  # Convert the second list's value to integer
        
        # Check if the values are different
        if valueA != valueB:
            differenceCount += 1  # Increment the difference count if values are not equal
    
    # Step 5: Output result based on the difference count
    if differenceCount < 3:
        print("YES")  # Print "YES" if differences are less than 3
    else:
        print("NO")  # Print "NO" if differences are 3 or more

# Step 6: Execute the main function if this script is run directly
if __name__ == "__main__":
    doMain()
