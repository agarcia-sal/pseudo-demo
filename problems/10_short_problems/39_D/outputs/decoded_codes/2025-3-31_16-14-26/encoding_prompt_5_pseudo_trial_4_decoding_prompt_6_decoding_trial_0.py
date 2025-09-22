def check_differences():
    # Prompt the user to enter the first set of integers
    first_set = input()  # input for the first set of integers separated by spaces

    # Prompt the user to enter the second set of integers
    second_set = input()  # input for the second set of integers separated by spaces

    # Split the input strings into separate integer values
    first_array = first_set.split()  # split based on spaces
    second_array = second_set.split()  # split based on spaces
    
    # Initialize a counter to track the number of differences
    difference_count = 0 

    # Loop through each index from 0 to 2 (for the three integers)
    for index in range(3):  # range(3) loops through 0, 1, and 2
        # Convert the strings at the current index to integers
        first_value = int(first_array[index])  # convert to integer
        second_value = int(second_array[index])  # convert to integer

        # Check if the two values differ
        if first_value != second_value:  # check for inequality
            difference_count += 1  # increment the difference counter

    # After comparing all integers, check the number of differences
    if difference_count < 3:  # if there are fewer than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Call the function to execute the comparisons
check_differences()
