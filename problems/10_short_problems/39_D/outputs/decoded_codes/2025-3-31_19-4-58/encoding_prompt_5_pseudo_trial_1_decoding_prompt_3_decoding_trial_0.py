def main():
    # Accept input for two sequences of numbers
    first_sequence = input()  # Read the first sequence from user
    second_sequence = input()  # Read the second sequence from user

    # Split the input sequences into lists of numbers
    first_list = first_sequence.split()  # Create a list from the first sequence
    second_list = second_sequence.split()  # Create a list from the second sequence

    # Initialize a counter for differences
    difference_count = 0 

    # Iterate over the range of the list indices (0 to 2, inclusive)
    for index in range(3):  # Loop over index 0, 1, and 2
        # Compare the two numbers in their integer form
        if int(first_list[index]) != int(second_list[index]):
            # Increment the counter if they are different
            difference_count += 1 

    # Check if the number of differences is less than 3
    if difference_count < 3:
        # Output "YES" if fewer than 3 differences are found
        print("YES")
    else:
        # Output "NO" if 3 or more differences are found
        print("NO")

# Execute the main function as the starting point of the program
main()
