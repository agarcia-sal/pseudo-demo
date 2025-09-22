def check_similarity():
    # Prompt user for first set of integers and store in variable firstSet
    first_set = input()
    # Prompt user for second set of integers and store in variable secondSet
    second_set = input()

    # Split the input strings into individual integers and convert to list of integers
    first_list = list(map(int, first_set.split()))
    second_list = list(map(int, second_set.split()))

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the integers in both lists
    for index in range(3):
        # Compare the integers at the same index in both lists
        first_value = first_list[index]
        second_value = second_list[index]

        # Check if the integers are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1 

    # If the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
check_similarity()
