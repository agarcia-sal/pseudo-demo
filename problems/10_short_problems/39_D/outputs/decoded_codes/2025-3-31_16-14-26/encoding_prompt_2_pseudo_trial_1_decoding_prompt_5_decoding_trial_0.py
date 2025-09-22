def doMain():
    # Prompt for user input
    inputString1 = input()  # Read first line of input
    inputString2 = input()  # Read second line of input

    # Process the input
    listOfValues1 = inputString1.split()  # Split the first input string into a list
    listOfValues2 = inputString2.split()  # Split the second input string into a list

    # Initialize a counter for the differences
    differenceCount = 0  # This will count how many corresponding values are different

    # Compare values at each index
    for index in range(3):  # Loop through indices 0 to 2
        valueA = int(listOfValues1[index])  # Convert the value in the first list to an integer
        valueB = int(listOfValues2[index])  # Convert the value in the second list to an integer
        if valueA != valueB:  # Check for differences
            differenceCount += 1  # Increment the counter if values are different

    # Output the result based on the difference count
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Start the program
if __name__ == "__main__":
    doMain()  # Execute the main procedure
