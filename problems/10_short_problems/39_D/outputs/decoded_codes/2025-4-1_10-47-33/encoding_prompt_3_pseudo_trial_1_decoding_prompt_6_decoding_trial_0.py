def do_main():
    # Read input values for two test cases
    first_test_case = input()  # User inputs first test case
    second_test_case = input()  # User inputs second test case
    
    # Split the input strings into lists of strings
    first_test_list = first_test_case.split()  # Convert the first test case into a list of substrings
    second_test_list = second_test_case.split()  # Convert the second test case into a list of substrings

    # Initialize count of differences
    difference_count = 0

    # Compare corresponding elements of both test cases
    for index in range(3):  # Loop through the first three indices
        value_from_first_test = int(first_test_list[index])  # Convert the string to an integer
        value_from_second_test = int(second_test_list[index])  # Convert the string to an integer
        
        # Check if the values from both test cases are different
        if value_from_first_test != value_from_second_test:
            difference_count += 1  # Increment difference count if values differ

    # Decide if the number of differences is acceptable
    if difference_count < 3:
        print("YES")  # Output YES if differences are less than 3
    else:
        print("NO")  # Output NO if differences are 3 or more

# Execute the main function if the script is run directly
if __name__ == "__main__":
    do_main()
