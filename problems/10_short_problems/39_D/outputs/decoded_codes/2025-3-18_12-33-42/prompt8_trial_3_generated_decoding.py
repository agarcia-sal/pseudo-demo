def main():
    # Get user input for two sets of values
    first_input = input()
    second_input = input()

    # Split the inputs into lists of strings
    first_values = first_input.split()
    second_values = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the range of the first three values (0 to 2)
    for index in range(3):
        # Convert the current values to integers
        value_from_first = int(first_values[index])
        value_from_second = int(second_values[index])

        # Check if the values from both inputs are different
        if value_from_first != value_from_second:
            # Increment the difference counter
            difference_count += 1

    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")   # Three or more differences

# Execute the main function
main()


     1 2 3
     1 2 3
     

     1 2 3
     1 5 3
     

     4 5 6
     7 5 8
     

     1 2 3
     4 5 6
     

     0 0 0
     0 0 1
     