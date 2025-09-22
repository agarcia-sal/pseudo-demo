def main():
    # Read input from the user
    first_input = input()  # Read first string input
    second_input = input()  # Read second string input

    # Split input strings into lists
    first_list = first_input.split()  # Split first input into a list
    second_list = second_input.split()  # Split second input into a list

    # Initialize a counter for differences
    difference_count = 0 

    # Check the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer

        # Compare elements and count differences
        if first_value != second_value:
            difference_count += 1  # Increment the difference count if they don't match

    # Determine result based on the number of differences
    if difference_count < 3:
        print("YES")  # Output YES if differences are less than 3
    else:
        print("NO")  # Output NO if differences are 3 or more

# Entry point of the program
if __name__ == "__main__":
    main()  # Call main function
