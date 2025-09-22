def main():
    # Read two input strings representing test results
    first_test_results = input()
    second_test_results = input()

    # Split the input strings into lists of strings
    first_test_list = first_test_results.split()
    second_test_list = second_test_results.split()

    # Initialize a counter to track the number of differences
    difference_count = 0

    # Iterate through the first three elements of both lists
    for index in range(3):  # Loop through indices 0, 1, and 2
        # Convert the elements from strings to integers
        first_test_value = int(first_test_list[index])
        second_test_value = int(second_test_list[index])

        # Check if the values are different
        if first_test_value != second_test_value:
            # Increment the difference counter
            difference_count += 1

    # Check the number of differences recorded
    if difference_count < 3:
        print("YES")  # Less than 3 differences means the tests are similar
    else:
        print("NO")   # 3 or more differences means the tests are different

# Execute the main function
main()


     1 2 3
     1 2 3
     

     YES
     

     1 2 3
     4 5 6
     

     NO
     

     1 2 3
     1 5 6
     

     YES
     

     2 3 4
     2 3 5
     

     YES
     