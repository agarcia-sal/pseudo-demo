def main():
    # Read input values from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of strings
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Initialize a variable to count differences
    differenceCount = 0 

    # Loop through each value in the lists (assuming they are of same length of 3)
    for index in range(3):
        # Convert string values to integers for comparison
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])

        # Check for differences between corresponding values
        if firstValue != secondValue:
            # Increment the difference count if values do not match
            differenceCount += 1

    # Decide the output based on the number of differences
    if differenceCount < 3:
        print("YES")  # Indicate that the inputs are similar enough
    else:
        print("NO")   # Indicate that the inputs are too different

# Main execution starts here
main()
