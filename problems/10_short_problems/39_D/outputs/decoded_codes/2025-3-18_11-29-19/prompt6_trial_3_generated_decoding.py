def main():
    # Read two lines of input
    first_input = input()  # Input for the first list
    second_input = input()  # Input for the second list

    # Split the input strings into lists of substrings
    first_list = first_input.split()  # Convert first input into a list of strings
    second_list = second_input.split()  # Convert second input into a list of strings

    # Initialize a counter for differences
    difference_count = 0

    # Iterate over the first three elements of both lists 
    for index in range(3):  # Loop through the index 0 to 2 (inclusive)
        # Convert elements to integers for comparison
        element_from_first_list = int(first_list[index])  # Convert string to integer
        element_from_second_list = int(second_list[index])  # Convert string to integer

        # Check if the elements are different
        if element_from_first_list != element_from_second_list:  # Compare the two elements
            # Increment the difference counter
            difference_count += 1  # Increase the counter if they are different

    # Determine the output based on the number of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Entry point of the program
if __name__ == "__main__":  # Check if the script is executed as main
    main()  # Call the main function
