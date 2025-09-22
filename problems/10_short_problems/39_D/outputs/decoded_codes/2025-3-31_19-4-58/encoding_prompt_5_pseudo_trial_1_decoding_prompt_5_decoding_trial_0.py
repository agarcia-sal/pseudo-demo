def main():
    # Accept input for two sequences of numbers from the user
    first_sequence = input()
    second_sequence = input()

    # Split the input sequences into lists of numbers
    first_list = first_sequence.split()
    second_list = second_sequence.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Iterate over the range of the list indices (0 to 2, inclusive)
    for index in range(3):
        # Convert the elements at the current index to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # Compare the two numbers
        if first_number != second_number:
            # Increment the counter if they are different
            difference_count += 1 

    # Check if the number of differences is less than 3
    if difference_count < 3:
        # Print "YES" if fewer than 3 differences are found
        print("YES")
    else:
        # Print "NO" if 3 or more differences are found
        print("NO")

# Execute the main function as the starting point of the program
main()
