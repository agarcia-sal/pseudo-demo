def do_main():
    # Get user input for two sets of three values
    first_input = input()
    second_input = input()

    # Split the inputs into lists of values
    first_values = first_input.split()
    second_values = second_input.split()

    # Initialize the mismatch counter
    mismatch_count = 0 

    # Compare the corresponding values from both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the values to integers for comparison
        first_value = int(first_values[index])
        second_value = int(second_values[index])

        # Check if the values do not match
        if first_value != second_value:
            # Increment the mismatch counter
            mismatch_count += 1 

    # Determine if the number of mismatches is less than 3
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    do_main()
