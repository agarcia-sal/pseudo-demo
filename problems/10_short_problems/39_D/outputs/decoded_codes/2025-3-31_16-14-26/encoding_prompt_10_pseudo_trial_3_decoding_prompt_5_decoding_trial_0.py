def do_main():
    # Initialize variables
    first_input = input()  # Get the first line of input
    second_input = input()  # Get the second line of input
    result_counter = 0  # Initialize a counter for differences

    # Split input strings into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Loop through the first 3 elements of both input lists
    for index in range(3):
        # Convert elements to integers
        value_a = int(first_list[index])
        value_b = int(second_list[index])

        # Compare values and update result counter if they are not equal
        if value_a != value_b:
            result_counter += 1

    # Check result to determine output
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
do_main()
