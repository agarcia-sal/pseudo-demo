def main():
    # Receive Input
    firstList = input()  # Read first list input from the user
    secondList = input()  # Read second list input from the user

    # Split Input into Lists
    firstElements = firstList.split()  # Split first list into elements
    secondElements = secondList.split()  # Split second list into elements

    # Initialize a Counter
    differenceCount = 0  # Counter for differences

    # Compare Corresponding Elements
    for index in range(3):  # Loop to compare elements at index 0 to 2
        currentFirstValue = int(firstElements[index])  # Convert to int
        currentSecondValue = int(secondElements[index])  # Convert to int
        if currentFirstValue != currentSecondValue:  # Check for differences
            differenceCount += 1  # Increment counter if different

    # Check Number of Differences
    if differenceCount < 3:
        print("YES")  # Output if differences are less than 3
    else:
        print("NO")  # Output if differences are 3 or more

# Invoke Main Function to Begin Execution
main()
