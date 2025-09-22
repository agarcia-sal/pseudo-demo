def doMain():
    # Input Handling
    inputString1 = input()  # Read the first line of input
    inputString2 = input()  # Read the second line of input
    
    # Split the input strings into lists of strings
    numberList1 = inputString1.split()
    numberList2 = inputString2.split()
    
    # Initialize a Counter for differences
    differenceCount = 0  # Count the number of differences

    # Comparison Logic
    for i in range(3):  # Loop over the first three elements (indices 0 to 2)
        valueA = int(numberList1[i])  # Convert element from the first list to integer
        valueB = int(numberList2[i])  # Convert element from the second list to integer
        
        # Check for differences
        if valueA != valueB:
            differenceCount += 1  # Increment the difference count if the values are not equal

    # Output Decision
    if differenceCount < 3:
        print("YES")  # Print "YES" if the differences are less than 3
    else:
        print("NO")  # Print "NO" if the differences are 3 or more

# Program Execution
if __name__ == "__main__":  # Check if this is the main module being executed
    doMain()  # Call the main function to execute
