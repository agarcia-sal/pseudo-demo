def main():
    # Read input values for two test cases
    test_case1 = input()
    test_case2 = input()

    # Split the input strings into lists of values
    values1 = test_case1.split()
    values2 = test_case2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare corresponding elements from the two lists
    for index in range(3):  # Assuming we compare the first three values
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
main()


Input:
1 2 3
1 2 4
Output:
YES


Input:
1 2 3
4 5 6
Output:
NO


Input:
7 8 9
7 10 11
Output:
YES
