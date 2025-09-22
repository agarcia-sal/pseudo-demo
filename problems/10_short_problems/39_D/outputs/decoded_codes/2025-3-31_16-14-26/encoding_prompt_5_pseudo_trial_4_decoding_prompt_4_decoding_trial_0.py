def check_differences():
    # Prompt the user to enter the first set of integers
    print("Enter the first set of three integers separated by spaces:")
    first_set = input()  # Accepting input as a string

    # Prompt the user to enter the second set of integers
    print("Enter the second set of integers separated by spaces:")
    second_set = input()  # Accepting input as a string

    # Split the input strings into separate integer values
    first_array = list(map(int, first_set.split()))  # Convert to list of integers
    second_array = list(map(int, second_set.split()))  # Convert to list of integers

    # Initialize a counter to track the number of differences
    difference_count = 0 

    # Loop through each index for the three integers
    for index in range(3):  # Iterate over the indices 0 to 2
        # Compare corresponding values from both arrays
        if first_array[index] != second_array[index]:
            difference_count += 1  # Increment the counter if they differ

    # After comparing all integers, check the number of differences
    if difference_count < 3:
        print("YES")  # Output "YES" if there are fewer than 3 differences
    else:
        print("NO")   # Output "NO" if there are 3 or more differences

# Call the function to execute the comparisons
check_differences()
