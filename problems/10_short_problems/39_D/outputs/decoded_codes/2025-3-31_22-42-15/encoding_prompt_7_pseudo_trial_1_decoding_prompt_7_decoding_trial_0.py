def doMain():
    # Read input values
    firstInput = input()  # Input for the first line
    secondInput = input()  # Input for the second line

    # Split inputs into lists of strings
    list1 = firstInput.split()  # Split the first input by spaces
    list2 = secondInput.split()  # Split the second input by spaces

    # Initialize a variable to count differences
    differenceCount = 0  # Counter for differing elements

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        valueA = int(list1[index])  # Convert the current element of list1 to integer
        valueB = int(list2[index])  # Convert the current element of list2 to integer

        # Check if the two values are different
        if valueA != valueB:
            # Increment the count of differences
            differenceCount += 1

    # Check the count of differences
    if differenceCount < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO if differences are 3 or more

# Execution starts here
if __name__ == "__main__":
    doMain()
