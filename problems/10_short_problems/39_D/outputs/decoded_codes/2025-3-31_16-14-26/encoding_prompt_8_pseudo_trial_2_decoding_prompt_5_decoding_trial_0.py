def check_similarity():
    # Read input values for two sets of integers
    first_set = input()
    second_set = input()

    # Split the input strings into individual integers
    first_list = first_set.split()
    second_list = second_set.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the integers in both lists
    for index in range(3):
        # Convert string values to integers for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])

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
