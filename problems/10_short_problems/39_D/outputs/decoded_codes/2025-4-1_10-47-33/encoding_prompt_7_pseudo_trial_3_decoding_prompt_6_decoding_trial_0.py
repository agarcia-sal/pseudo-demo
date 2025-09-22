def main():
    # Read input for two sets of numbers
    first_input = input()  # Input the first set of numbers
    second_input = input()  # Input the second set of numbers

    # Split the input strings into lists of numbers
    first_list = first_input.split()  # Split the first input
    second_list = second_input.split()  # Split the second input

    # Initialize a counter for differences
    difference_count = 0 

    # Compare the first three numbers in both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the current elements to integers
        first_number = int(first_list[index])  # Convert to integer
        second_number = int(second_list[index])  # Convert to integer

        # Check if the numbers are different
        if first_number != second_number:  # If numbers are not equal
            # Increment the differences counter
            difference_count += 1  # Count the difference

    # Determine output based on the number of differences
    if difference_count < 3:  # If differences are fewer than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Entry point for the program
if __name__ == "__main__":
    main()  # Call main function when the script is executed
