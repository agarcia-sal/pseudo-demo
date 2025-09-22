def main():
    # Get input from the user for two sets of data
    firstInput = input()  # First line of input
    secondInput = input()  # Second line of input

    # Split the inputs into lists of strings
    firstList = firstInput.split()  # Split string by whitespace
    secondList = secondInput.split()  # Split string by whitespace

    # Initialize a counter to track differences
    differenceCount = 0

    # Compare the first three elements from both lists
    for index in range(3):  # Loop through first three elements (indices 0, 1, 2)
        # Convert the current elements to integers
        firstValue = int(firstList[index])  # Convert the first list element to int
        secondValue = int(secondList[index])  # Convert the second list element to int
        
        # Check if the values are different
        if firstValue != secondValue:  # Compare the two integers
            differenceCount += 1  # Increment the counter if values differ

    # Decide output based on the number of differences found
    if differenceCount < 3:  # If differences are less than 3
        print("YES")  # Print YES
    else:
        print("NO")  # Print NO if there are 3 or more differences

# Entry point of the program
main()  # Call the main function to execute the program
