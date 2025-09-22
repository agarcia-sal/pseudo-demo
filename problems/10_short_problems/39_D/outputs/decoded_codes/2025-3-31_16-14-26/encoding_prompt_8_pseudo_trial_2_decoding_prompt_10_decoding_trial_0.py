def check_similarity():
    # Read input values for two sets of integers from the user
    first_set = input()
    second_set = input()

    # Split the input strings into lists of integers
    first_list = list(map(int, first_set.split()))
    second_list = list(map(int, second_set.split()))

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the integers in both lists to count differences
    for index in range(3):
        first_value = first_list[index]
        second_value = second_list[index]

        # Check if the integers are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1

    # Output decision based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
check_similarity()
