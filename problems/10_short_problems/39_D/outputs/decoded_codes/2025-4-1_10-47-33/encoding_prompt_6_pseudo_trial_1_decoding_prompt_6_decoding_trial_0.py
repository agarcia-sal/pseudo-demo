def main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()

    # Split the input lines into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()

    # Initialize a variable to count the number of differences
    difference_count = 0

    # Loop through the first three elements of the lists
    for index in range(3):
        # Convert the string values at the current index to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Check if the values from both lists are different
        if first_value != second_value:
            # If they are different, increment the difference count
            difference_count += 1

    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
