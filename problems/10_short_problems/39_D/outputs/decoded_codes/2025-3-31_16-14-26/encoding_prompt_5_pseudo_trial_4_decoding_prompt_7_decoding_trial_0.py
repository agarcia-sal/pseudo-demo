def checkDifferences():
    # Prompt the user to enter the first set of integers
    print("Enter the first set of three integers separated by spaces:")
    firstSet = input()  # Take the input for the first set

    # Prompt the user to enter the second set of integers
    print("Enter the second set of three integers separated by spaces:")
    secondSet = input()  # Take the input for the second set

    # Split the input strings into separate integer values
    firstArray = firstSet.split()  # Split first input
    secondArray = secondSet.split()  # Split second input
    
    # Initialize a counter to track the number of differences
    difference_count = 0 

    # Loop through each index from 0 to 2 (for the three integers)
    for index in range(3):  # 0, 1, 2
        # Convert the strings at the current index to integers
        first_value = int(firstArray[index])  # Convert string to integer for first set
        second_value = int(secondArray[index])  # Convert string to integer for second set

        # Check if the two values differ
        if first_value != second_value:
            difference_count += 1  # Increment count if values are not equal

    # After comparing all integers, check the number of differences
    if difference_count < 3:
        print("YES")  # Output "YES" if there are fewer than 3 differences
    else:
        print("NO")  # Output "NO" if there are 3 or more differences

# Call the function to execute the comparisons
checkDifferences()
