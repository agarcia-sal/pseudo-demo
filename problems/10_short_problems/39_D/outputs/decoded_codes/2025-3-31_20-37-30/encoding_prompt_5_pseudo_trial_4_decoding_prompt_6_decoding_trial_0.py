def doMain():
    # Accept input values from the user
    first_input = input()  # Read the first line of input
    second_input = input()  # Read the second line of input

    # Split input strings into lists of values
    first_values = first_input.split()  # Split the first input into a list
    second_values = second_input.split()  # Split the second input into a list

    # Initialize a counter to track differences
    difference_count = 0  # Set the initial difference count to 0

    # Compare value pairs from the two lists
    for index in range(3):  # Loop over the first three indices
        # Convert values to integers for comparison
        first_value = int(first_values[index])  # Convert first value to int
        second_value = int(second_values[index])  # Convert second value to int
        
        # Check for differences
        if first_value != second_value:  # If values are not equal
            difference_count += 1  # Increment the difference count

    # Output the result based on the number of differences
    if difference_count < 3:  # If fewer than 3 differences
        print("YES")  # Print YES
    else:  
        print("NO")  # Otherwise, print NO

# Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()  # Call the main function
