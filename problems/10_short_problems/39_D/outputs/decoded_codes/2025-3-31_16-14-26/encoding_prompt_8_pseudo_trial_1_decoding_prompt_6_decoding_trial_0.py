def main():
    # Receive two lines of input from the user
    first_input = input()  # Take the first line of input
    second_input = input()  # Take the second line of input
    
    # Split each input into a list of strings
    first_list = first_input.split()  # Create a list from the first input
    second_list = second_input.split()  # Create a list from the second input
    
    # Initialize a counter for differences
    difference_count = 0  # Counter for tracking number of differences

    # Loop through each corresponding pair in the two lists
    for index in range(3):  # Looping through indices 0 to 2
        # Convert the string at the current index to an integer for both lists
        first_value = int(first_list[index])  # Convert first list value
        second_value = int(second_list[index])  # Convert second list value

        # Check if the values are different
        if first_value != second_value:  # If the values differ
            # Increment the difference counter
            difference_count += 1

    # After comparing all three values, check the count of differences
    if difference_count < 3:  # If differences are fewer than 3
        print("YES")  # Output that the values are similar
    else:
        print("NO")  # Output that the values are different

# Entry point for the program
if __name__ == "__main__":
    main()  # Call the main function to execute the program
