def do_main():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()

    # Split the inputs into lists of values
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare corresponding elements in both lists
    for index in range(3):  # since we want to compare the first three elements
        # Convert the current elements to integers for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1 

    # Output result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
do_main()
