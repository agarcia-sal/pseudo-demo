def checkDifferences():
    # Prompt the user to enter the first set of integers
    print("Enter the first set of three integers separated by spaces:")
    firstSet = input()

    # Prompt the user to enter the second set of integers
    print("Enter the second set of integers separated by spaces:")
    secondSet = input()

    # Split the input strings into separate integer values
    firstArray = firstSet.split()
    secondArray = secondSet.split()
    
    # Initialize a counter to track the number of differences
    difference_count = 0 

    # Loop through each index from 0 to 2 (for the three integers)
    for index in range(3):
        # Convert the strings at the current index to integers
        first_value = int(firstArray[index])
        second_value = int(secondArray[index])

        # Check if the two values differ
        if first_value != second_value:
            difference_count += 1

    # After comparing all integers, check the number of differences
    if difference_count < 3:
        print("YES")    # Output "YES" if there are fewer than 3 differences
    else:
        print("NO")     # Output "NO" if there are 3 or more differences

# Call the function to execute the comparisons
checkDifferences()


def checkDifferences():
    print("Enter the sets of integers separated by spaces (enter 3 integers for each set):")
    firstSet = input()
    secondSet = input()

    firstArray = firstSet.split()
    secondArray = secondSet.split()

    if len(firstArray) != len(secondArray):  # Validation step
        print("The number of integers in both sets must be equal.")
        return

    difference_count = sum(1 for a, b in zip(firstArray, secondArray) if a != b)

    if difference_count < len(firstArray) // 2:  # Update condition for any size
        print("YES")
    else:
        print("NO")

checkDifferences()
