def compare_two_sets_of_numbers():
    # Step 1: Get user input for two sets of numbers
    first_set = input()  # Enter first set of numbers (separated by spaces)
    second_set = input()  # Enter second set of numbers (separated by spaces)

    # Step 2: Split each set of numbers into individual elements
    first_list = first_set.split()  # Convert string input to a list of strings
    second_list = second_set.split()  # Convert string input to a list of strings

    # Step 3: Initialize a counter to track differences
    difference_count = 0 

    # Step 4: Compare corresponding numbers in both sets
    for index in range(3):  # We know there are exactly three numbers in each set
        # Convert string to integer for comparison
        number_from_first_set = int(first_list[index])
        number_from_second_set = int(second_list[index])

        # Step 5: Check if the numbers are different
        if number_from_first_set != number_from_second_set:
            difference_count += 1  # Increment difference count if they are not equal

    # Step 6: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # The sets are sufficiently similar
    else:
        print("NO")   # The sets are too different

# Main execution
compare_two_sets_of_numbers()
