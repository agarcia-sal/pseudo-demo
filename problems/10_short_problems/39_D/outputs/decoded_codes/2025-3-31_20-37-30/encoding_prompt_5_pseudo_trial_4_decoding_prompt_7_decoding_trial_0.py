def doMain():
    # Accept input for the first and second lists of numbers
    firstInput = input()  # Read the first line of input
    secondInput = input()  # Read the second line of input

    # Split input strings into lists of values
    firstValues = firstInput.split()  # Split first input into a list
    secondValues = secondInput.split()  # Split second input into a list

    # Initialize a counter for the number of differing values
    differenceCount = 0  

    # Compare values at corresponding positions in the two lists
    for x in range(3):  # Loop through indices 0 to 2
        # Convert the string values to integers for comparison
        firstValue = int(firstValues[x])  
        secondValue = int(secondValues[x])  
        
        # Increment the difference count if the values are not equal
        if firstValue != secondValue:
            differenceCount += 1  

    # Output the result based on the number of differences
    if differenceCount < 3:
        print("YES")  # Fewer than 3 differences
    else:
        print("NO")  # 3 or more differences

# Execute the main function if this script is run directly
if __name__ == "__main__":
    doMain()
