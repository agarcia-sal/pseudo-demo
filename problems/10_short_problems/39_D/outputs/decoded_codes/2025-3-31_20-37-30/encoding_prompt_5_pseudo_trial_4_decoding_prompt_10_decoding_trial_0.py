def doMain():
    # Accept input from user
    first_input = input()
    second_input = input()

    # Split the input values into lists
    first_values = first_input.split()
    second_values = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Compare values at each index
    for index in range(3):  # We assume there are exactly three values
        first_value = int(first_values[index])  # Convert to integer
        second_value = int(second_values[index])  # Convert to integer

        # Increment difference count if values don't match
        if first_value != second_value:
            difference_count += 1

    # Output the result based on the difference count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run as the main program
if __name__ == "__main__":
    doMain()
