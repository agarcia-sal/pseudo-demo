def main():
    # Read input values from the user
    first_input = input()
    second_input = input()

    # Split the inputs into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize the difference count
    difference_count = 0

    # Compare corresponding elements of the two lists
    for index in range(3):  # only until index 2
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer

        # Increment difference count if values are not equal
        if first_value != second_value:
            difference_count += 1

    # Output based on the difference count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
