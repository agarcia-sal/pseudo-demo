def do_main():
    # Read input values for two test cases
    first_test_case = input()
    second_test_case = input()
    
    # Split the input strings into lists of strings
    first_test_list = first_test_case.split()
    second_test_list = second_test_case.split()

    # Initialize count of differences
    difference_count = 0

    # Compare corresponding elements of both test cases
    for index in range(3):
        value_from_first_test = int(first_test_list[index])
        value_from_second_test = int(second_test_list[index])
        
        # Check if the values from both test cases are different
        if value_from_first_test != value_from_second_test:
            difference_count += 1

    # Decide if the number of differences is acceptable
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    do_main()
