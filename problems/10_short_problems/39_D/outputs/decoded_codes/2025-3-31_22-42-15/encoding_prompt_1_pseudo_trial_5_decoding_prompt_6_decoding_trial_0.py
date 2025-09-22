def main():
    # Read input values for two test cases
    test_case_1 = input()  # User input for the first test case
    test_case_2 = input()  # User input for the second test case

    # Split the input strings into lists of values
    values_1 = test_case_1.split()  # Split the first test case by spaces
    values_2 = test_case_2.split()  # Split the second test case by spaces

    # Initialize a counter for differences
    difference_count = 0  # Counter for the number of differing values

    # Compare corresponding elements from the two lists
    for index in range(3):  # Loop for indices 0 to 2
        # Convert string values to integers
        value_1 = int(values_1[index])  # Convert to integer
        value_2 = int(values_2[index])  # Convert to integer

        # Check if the values are different
        if value_1 != value_2:  # Check if they are not equal
            difference_count += 1  # Increment the difference counter

    # Determine the output based on the number of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Execute the main function when the program starts
main()
