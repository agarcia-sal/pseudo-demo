def doMain():
    # Collect inputs from the user
    firstInput = input()  # Get user input for the first sequence
    secondInput = input()  # Get user input for the second sequence

    # Split the inputs into lists of strings
    firstList = firstInput.split()  # Split first input into a list of words
    secondList = secondInput.split()  # Split second input into a list of words

    # Initialize a counter for differences
    differenceCount = 0

    # Compare elements from both lists
    for index in range(3):  # Iterate from 0 to 2 (inclusive)
        # Convert string values to integers
        firstValue = int(firstList[index])  # Convert first list element to integer
        secondValue = int(secondList[index])  # Convert second list element to integer

        # Increment the difference count if values are not equal
        if firstValue != secondValue:  # Check for inequality
            differenceCount += 1  # Increment the difference count

    # Determine final output based on the number of differences
    if differenceCount < 3:  # If there are less than 3 differences
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO if differences are 3 or more

# Main execution starts here
if __name__ == "__main__":  # Ensure this script runs only if executed directly
    doMain()  # Call the main function
