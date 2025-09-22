def compare_inputs():
    # Get the first set of three numbers from the user
    print("Enter the first set of numbers:")
    first_input = input()
    
    # Get the second set of three numbers from the user
    print("Enter the second set of numbers:")
    second_input = input()

    # Split the input strings into lists of numbers
    first_set = first_input.split()
    second_set = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through each position of the sets (0 to 2)
    for index in range(3):
        # Convert the numbers at the current index to integers
        first_number = int(first_set[index])
        second_number = int(second_set[index])

        # If the numbers are different, increment the difference counter
        if first_number != second_number:
            difference_count += 1

    # If the number of differences is less than 3, print "YES"
    if difference_count < 3:
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Start the program
compare_inputs()
