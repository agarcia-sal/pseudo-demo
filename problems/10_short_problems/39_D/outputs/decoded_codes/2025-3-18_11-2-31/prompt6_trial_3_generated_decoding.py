def do_main():
    # Read two lines of input
    first_input = input()
    second_input = input()

    # Split the input strings into lists of strings
    first_number_list = first_input.split()
    second_number_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare the first three elements of both lists
    for index in range(3):  # Looping from 0 to 2 inclusive
        # Convert the current elements to integers
        first_number = int(first_number_list[index])
        second_number = int(second_number_list[index])
        
        # Check if the current elements are different
        if first_number != second_number:
            # Increment the difference count
            difference_count += 1 

    # Determine if there are fewer than 3 differences
    if difference_count < 3:
        print("YES")  # Fewer than 3 differences
    else:
        print("NO")   # 3 or more differences

# Start the program by calling do_main
do_main()
