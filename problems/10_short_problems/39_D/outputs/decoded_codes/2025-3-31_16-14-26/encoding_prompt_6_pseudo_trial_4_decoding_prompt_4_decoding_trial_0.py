def main():
    # Get inputs from the user
    first_string = input()
    second_string = input()

    # Split the input strings into lists of words
    first_list = first_string.split()
    second_list = second_string.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the corresponding elements to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # Check if the numbers are different
        if first_number != second_number:
            # Increment the difference counter
            difference_count += 1

    # Check the number of differences found
    if difference_count < 3:
        print("YES")
    else:
        print("NO")


# Execute the main function
main()
