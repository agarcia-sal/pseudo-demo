def main():
    # Read input values for two test cases
    test_case_1 = input()  # Get user input
    test_case_2 = input()  # Get user input

    # Split the input strings into lists of values
    values_1 = test_case_1.split()  # Split by spaces
    values_2 = test_case_2.split()  # Split by spaces

    # Ensure that the lengths of both lists are equal to 3 for comparison
    if len(values_1) != 3 or len(values_2) != 3:
        print("Input must contain exactly three numbers for each test case.")
        return

    # Initialize a counter for differences
    difference_count = 0

    # Compare corresponding elements from the two lists
    for index in range(3):
        # Convert string values to integers
        value_1 = int(values_1[index])  # Convert to integer
        value_2 = int(values_2[index])  # Convert to integer

        # Check if the values are different
        if value_1 != value_2:
            difference_count += 1  # Increment the counter

    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()
