def do_main():
    # Read two lines of input
    input_line_1 = input()  # Read first input line
    input_line_2 = input()  # Read second input line

    # Split the input lines into lists of strings
    list_1 = input_line_1.split()  # Split first line into a list of strings
    list_2 = input_line_2.split()  # Split second line into a list of strings

    # Initialize a counter for differences
    difference_count = 0  # Counter for differences

    # Compare elements of both lists
    for index in range(3):  # Loop through the first three elements
        value_1 = int(list_1[index])  # Convert string to integer from first list
        value_2 = int(list_2[index])  # Convert string to integer from second list

        # Increment the difference count if values are not equal
        if value_1 != value_2:  # Check if values are not equal
            difference_count += 1  # Increment difference count

    # Check the number of differences and print result
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Print YES
    else:
        print("NO")  # Print NO

# Start the program
if __name__ == "__main__":  # Check if this script is the main module
    do_main()  # Call the function
