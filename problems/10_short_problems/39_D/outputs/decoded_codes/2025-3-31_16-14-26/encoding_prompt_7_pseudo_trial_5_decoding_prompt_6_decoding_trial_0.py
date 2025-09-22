def main_function():
    # Prompt the user for input
    first_input = input()  # Get first string input from user
    second_input = input()  # Get second string input from user

    # Split the input strings into lists of substrings
    first_list = first_input.split()  # Split first input into a list
    second_list = second_input.split()  # Split second input into a list
    
    # Initialize a counter for differences
    difference_count = 0  # Counter for differing values

    # Compare corresponding elements in the two lists
    for index in range(3):  # Loop from index 0 to 2
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer

        # Check if the values differ
        if first_value != second_value:  # If values are not equal
            difference_count += 1  # Increment the difference counter

    # Determine the output based on the number of differences
    if difference_count < 3:  # If fewer than 3 differences
        print("YES")  # Output YES
    else:  # If 3 or more differences
        print("NO")  # Output NO

# Initiates the main_function when the script is executed
if __name__ == "__main__":
    main_function()  # Call the main function to execute
