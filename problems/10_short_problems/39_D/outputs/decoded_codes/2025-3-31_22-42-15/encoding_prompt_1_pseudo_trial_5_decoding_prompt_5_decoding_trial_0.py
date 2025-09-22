def main():
    # Read input values for two test cases
    test_case_1 = input()
    test_case_2 = input()

    # Split the input strings into lists of values
    values_1 = test_case_1.split()
    values_2 = test_case_2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare corresponding elements from the two lists
    for index in range(3):  # Since we are comparing only three elements
        # Convert string values to integers
        value_1 = int(values_1[index])
        value_2 = int(values_2[index])

        # Check if the values are different
        if value_1 != value_2:
            difference_count += 1 

    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()
