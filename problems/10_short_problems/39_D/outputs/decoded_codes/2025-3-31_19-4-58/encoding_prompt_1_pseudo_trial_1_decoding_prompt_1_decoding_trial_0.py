def main():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Check if the current elements are different
        if first_value != second_value:
            # Increment the difference count
            difference_count += 1

    # Check if the number of differences is less than three
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
