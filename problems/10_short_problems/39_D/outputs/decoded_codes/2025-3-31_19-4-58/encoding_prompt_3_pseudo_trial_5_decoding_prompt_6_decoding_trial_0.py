def main():
    # Read input from the user
    first_input = input()  # First line of input
    second_input = input()  # Second line of input

    # Split the input strings into lists of values
    first_list = first_input.split()  # Split by spaces
    second_list = second_input.split()  # Split by spaces

    # Initialize a counter to track differences
    difference_count = 0  # Counter for differences

    # Loop through the first three values of both lists
    for index in range(3):  # Looping from 0 to 2 (inclusive)
        # Convert string values to integers
        value_from_first_list = int(first_list[index])  # Convert first list value to int
        value_from_second_list = int(second_list[index])  # Convert second list value to int

        # Check if the values are different
        if value_from_first_list != value_from_second_list:  # Compare values
            # Increment the difference counter
            difference_count += 1  # Increase counter if values differ

    # Check the number of differences and output the result
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Main execution starts here
main()  # Call the main function
