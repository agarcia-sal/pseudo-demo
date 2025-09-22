def do_main():
    # Read input values from the user
    first_input = input()
    second_input = input()

    # Split the inputs into lists of values
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a variable to count differences
    difference_count = 0

    # Compare corresponding elements of the two lists
    for index in range(3):  # Assuming both lists have at least 3 elements as per the pseudocode
        # Convert string values to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Count differences
        if first_value != second_value:
            difference_count += 1

    # Output the result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    do_main()
