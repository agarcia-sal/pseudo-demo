def main():
    # Read input values for two test cases
    test_case_1 = input()
    test_case_2 = input()
    
    # Split the input strings into lists of values
    values1 = test_case_1.split()
    values2 = test_case_2.split()
    
    # Initialize a counter for differences
    difference_count = 0

    # Compare corresponding elements from the two lists
    for index in range(3):  # Iterating through the first three elements
        # Convert string values to integers
        value1 = int(values1[index])
        value2 = int(values2[index])

        # Check if the values are different
        if value1 != value2:
            difference_count += 1
    
    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")


# Execute the main function when the program starts
if __name__ == "__main__":
    main()
