def doMain():
    # Step 2: Get Input Values
    firstInput = input()  # Read the first line of input
    secondInput = input()  # Read the second line of input

    # Step 3: Split Input into Lists
    firstValues = firstInput.split()  # Split the first input into a list of strings
    secondValues = secondInput.split()  # Split the second input into a list of strings

    # Step 4: Initialize Difference Counter
    differenceCount = 0  # Initialize the counter for differences

    # Step 5: Iterate and Count Differences
    for index in range(3):  # Loop through indices 0 to 2 inclusive
        valueA = int(firstValues[index])  # Convert to integer from first list
        valueB = int(secondValues[index])  # Convert to integer from second list
        
        # Check if the values are different
        if valueA != valueB:
            differenceCount += 1  # Increment difference count if values are not equal

    # Step 6: Decide Output Based on Count
    if differenceCount < 3:  # If less than 3 differences
        print("YES")  # Output affirmative result
    else:
        print("NO")  # Otherwise output negative result

# Step 7: Run Main Function if Script is Executed
if __name__ == "__main__":
    doMain()  # Start the program
