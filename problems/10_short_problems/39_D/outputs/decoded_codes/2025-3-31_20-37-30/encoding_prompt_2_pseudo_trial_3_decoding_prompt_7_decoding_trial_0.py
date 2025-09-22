def doMain():
    # Step 2: Input Collection
    firstInputString = input()  # Prompt for the first input string
    secondInputString = input()  # Prompt for the second input string

    # Step 3: String Splitting
    firstInputList = firstInputString.split()  # Split the first input string into a list
    secondInputList = secondInputString.split()  # Split the second input string into a list

    # Step 4: Result Initialization
    differenceCount = 0  # Initialize a count for differences

    # Step 5: Comparison Loop
    for index in range(3):  # Iterate over the first three elements
        firstValue = int(firstInputList[index])  # Convert first list value to integer
        secondValue = int(secondInputList[index])  # Convert second list value to integer
        if firstValue != secondValue:  # Compare values
            differenceCount += 1  # Increment difference count if values are not equal

    # Step 6: Result Evaluation
    if differenceCount < 3:  # Evaluate the number of differences
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" otherwise

# Step 7: Execution Trigger
if __name__ == "__main__":
    doMain()  # Execute the main function if the script is run directly
