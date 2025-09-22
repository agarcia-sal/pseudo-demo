def doMain():
    # Input Handling
    inputString1 = input()  # Read the first line of input
    inputString2 = input()  # Read the second line of input
    numberList1 = inputString1.split()  # Split inputString1 into a list of strings
    numberList2 = inputString2.split()  # Split inputString2 into a list of strings
    
    # Initialize a Counter
    differenceCount = 0  # Initialize the difference counter

    # Comparison Logic
    for i in range(3):  # Loop over indices 0 to 2
        valueA = int(numberList1[i])  # Convert to integer from numberList1
        valueB = int(numberList2[i])  # Convert to integer from numberList2
        if valueA != valueB:  # Check for differences
            differenceCount += 1  # Increment difference count if they are not equal

    # Output Decision
    if differenceCount < 3:  # Check against the threshold
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO if differences are 3 or more

# Program Execution
if __name__ == "__main__":  # Ensure this runs only if executed as the main program
    doMain()
