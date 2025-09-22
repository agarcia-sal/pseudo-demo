def main():
    # Get two input strings from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a variable to count differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the elements at the current index to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # If the values are different, increment the difference count
        if first_value != second_value:
            difference_count += 1

    # If the number of differences is less than 3, print "YES"; otherwise, print "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
