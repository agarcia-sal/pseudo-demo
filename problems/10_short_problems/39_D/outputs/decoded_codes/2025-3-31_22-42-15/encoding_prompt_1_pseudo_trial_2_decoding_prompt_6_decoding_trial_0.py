def doMain():
    # Step 2: Get Input Values
    firstInput = input()  # Read first set of values
    secondInput = input()  # Read second set of values

    # Step 3: Split Input into Lists
    firstValues = firstInput.split()  # Split first input string into a list
    secondValues = secondInput.split()  # Split second input string into a list

    # Step 4: Initialize a Difference Counter
    differenceCount = 0  # Initialize the difference counter to 0

    # Step 5: Iterate and Count Differences
    for index in range(3):  # Loop over the first three indices
        valueA = int(firstValues[index])  # Convert first value to integer
        valueB = int(secondValues[index])  # Convert second value to integer
        
        # Check if the values are different
        if valueA != valueB:
            differenceCount += 1  # Increase the difference count if they are not equal

    # Step 6: Decide Output Based on Count
    if differenceCount < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO if differences are 3 or more

# Step 7: Run Main Function if Script is Executed
if __name__ == "__main__":
    doMain()  # Call the main function to execute the program
