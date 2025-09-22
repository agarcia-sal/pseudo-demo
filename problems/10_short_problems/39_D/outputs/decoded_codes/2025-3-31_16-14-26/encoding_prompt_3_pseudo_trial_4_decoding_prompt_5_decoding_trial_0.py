def main():
    # Read input values from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of strings
    first_values = first_input.split()
    second_values = second_input.split()

    # Initialize a variable to count differences
    difference_count = 0 

    # Loop through each value in the lists (assuming they are of the same length of 3)
    for index in range(3):
        # Convert string values to integers for comparison
        first_value = int(first_values[index])
        second_value = int(second_values[index])

        # Check for differences between corresponding values
        if first_value != second_value:
            # Increment the difference count if values do not match
            difference_count += 1

    # Decide the output based on the number of differences
    if difference_count < 3:
        print("YES")  # Indicate that the inputs are similar enough
    else:
        print("NO")   # Indicate that the inputs are too different

# Main execution starts here
main()
