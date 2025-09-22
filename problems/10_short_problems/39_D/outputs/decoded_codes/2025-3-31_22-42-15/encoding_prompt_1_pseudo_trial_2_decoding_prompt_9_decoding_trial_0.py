def doMain():
    # Input Collection: Get Input Values
    firstInput = input()  # Read first line of input
    secondInput = input()  # Read second line of input
    
    # Data Preparation: Split Input into Lists
    firstValues = firstInput.split()  # Split the first input into a list
    secondValues = secondInput.split()  # Split the second input into a list
    
    # Initialize Counter: Set a Difference Counter
    differenceCount = 0
    
    # Comparison Loop: Iterate and Count Differences
    for index in range(3):  # Iterate through the first three indices
        valueA = int(firstValues[index])  # Convert to integer
        valueB = int(secondValues[index])  # Convert to integer
        if valueA != valueB:  # Check for differences
            differenceCount += 1  # Increase counter if different
    
    # Conditional Check: Decide Output Based on Count
    if differenceCount < 3:
        print("YES")  # Output if fewer than 3 differences
    else:
        print("NO")  # Output if 3 or more differences

# Program Execution: Run Main Function if Script is Executed
if __name__ == "__main__":
    doMain()  # Start the main function
