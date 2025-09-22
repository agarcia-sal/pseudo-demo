def compare_integers():
    # Get two sets of three integers from the user
    first_set = input()
    second_set = input()

    # Split the input strings into lists of integers
    first_list = list(map(int, first_set.split()))
    second_list = list(map(int, second_set.split()))

    # Initialize a counter for differences
    difference_count = 0 

    # Iterate through the first three integers in both lists
    for index in range(3):
        # Check if the values are different
        if first_list[index] != second_list[index]:
            # Increment the difference counter
            difference_count += 1 

    # Determine if the count of differences is less than three
    if difference_count < 3:
        print("YES")  # Indicate that the differences are acceptable
    else:
        print("NO")   # Indicate that there are too many differences

# Main process begins here
compare_integers()
