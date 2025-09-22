def main():
    # Read two input strings from the user
    first_input = input()  # Get user input for the first list
    second_input = input()  # Get user input for the second list

    # Split the input strings into lists of values
    first_list = first_input.split()  # Split first input by spaces
    second_list = second_input.split()  # Split second input by spaces

    # Initialize a counter for differences
    difference_count = 0  # Counter to track differences

    # Loop through the first three elements of each list
    for index in range(3):  # Looping through indices 0 to 2
        # Convert the current string elements to integers 
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer

        # Compare the values and increment the difference counter if they are not equal
        if first_value != second_value:  # Check for inequality
            difference_count += 1  # Increment difference count if not equal

    # Check the count of differences to determine the output
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Print YES
    else:
        print("NO")  # Otherwise, print NO

# Start the program
main()  # Call the main function to execute the program
