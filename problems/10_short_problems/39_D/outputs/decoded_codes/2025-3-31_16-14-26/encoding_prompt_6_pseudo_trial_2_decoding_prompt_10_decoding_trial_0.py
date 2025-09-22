def main():
    # Read two input strings from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of words
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize the difference counter
    difference_counter = 0

    # Loop through the first three items in both lists
    for index in range(3):
        # Convert the current items from the lists to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Check if the values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_counter += 1

    # If the count of differences is less than 3, print "YES"
    if difference_counter < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
