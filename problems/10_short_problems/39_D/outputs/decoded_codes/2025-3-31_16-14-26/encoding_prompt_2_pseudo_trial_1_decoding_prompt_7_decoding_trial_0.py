def doMain():
    # Prompt for User Input
    inputString1 = input()  # First input line
    inputString2 = input()  # Second input line

    # Process the Input
    listOfValues1 = inputString1.split()  # Split the first input into a list of strings
    listOfValues2 = inputString2.split()  # Split the second input into a list of strings

    # Initialize a Counter
    differenceCount = 0  # This will count the number of differing values

    # Compare Values
    for index in range(3):  # Loop through indexes 0 to 2
        valueA = int(listOfValues1[index])  # Convert corresponding value from first list to an integer
        valueB = int(listOfValues2[index])  # Convert corresponding value from second list to an integer
        if valueA != valueB:  # Check if the values are different
            differenceCount += 1  # Increment the difference count if they are different

    # Output the Result
    if differenceCount < 3:  # Check the difference count against the threshold
        print("YES")  # Output "YES" if less than 3 differences
    else:
        print("NO")  # Output "NO" if 3 or more differences

# Start the Program
if __name__ == "__main__":
    doMain()  # Execute the main procedure if this script is run standalone
