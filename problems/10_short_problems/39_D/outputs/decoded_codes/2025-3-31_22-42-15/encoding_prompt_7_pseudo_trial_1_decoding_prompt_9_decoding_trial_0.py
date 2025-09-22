def doMain():
    # Read input values
    firstInput = input()
    secondInput = input()
    
    # Split inputs into lists of strings
    list1 = firstInput.split()
    list2 = secondInput.split()

    # Initialize a variable to count differences
    differenceCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        valueA = int(list1[index])
        valueB = int(list2[index])

        # Check if the two values are different
        if valueA != valueB:
            # Increment the count of differences
            differenceCount += 1

    # Check the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execution starts here
if __name__ == "__main__":
    doMain()
