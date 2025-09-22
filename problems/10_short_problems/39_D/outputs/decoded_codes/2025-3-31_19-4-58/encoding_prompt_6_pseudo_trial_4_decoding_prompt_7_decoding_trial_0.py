def main():
    # Read two lines of input from the user
    firstInput = input()  # Read the first line of input
    secondInput = input()  # Read the second line of input
    
    # Split the input strings into lists of strings
    firstTokens = firstInput.split()  # Split the first input by spaces
    secondTokens = secondInput.split()  # Split the second input by spaces
    
    # Initialize a counter for differences
    differenceCount = 0  # Count the number of differences

    # Compare the corresponding elements of the two lists
    for index in range(3):  # Loop through the first three elements
        # Convert the token to an integer
        firstValue = int(firstTokens[index])  # Convert the first token to an integer
        secondValue = int(secondTokens[index])  # Convert the second token to an integer
        
        # Check if the values are different
        if firstValue != secondValue:  # If the values are not the same
            differenceCount += 1  # Increment the difference count

    # Determine and print the result based on the number of differences
    if differenceCount < 3:  # If there are less than three differences
        print("YES")  # Print YES
    else:  # If there are three or more differences
        print("NO")  # Print NO

# Execute the main function
main()
