def compare_integers():
    # Get two sets of three integers from the user
    first_set = input()
    second_set = input()

    # Split the input strings into lists of integers
    first_list = first_set.split()
    second_list = second_set.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Iterate through the first three integers in both lists
    for index in range(3):
        # Convert string values to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1 

    # Determine if the count of differences is less than three
    if difference_count < 3:
        print("YES")  # Indicate that the differences are acceptable
    else:
        print("NO")   # Indicate that there are too many differences

# Main process begins here
compare_integers()
