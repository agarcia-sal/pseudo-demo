def doMain():
    # Read input values
    first_input = input()
    second_input = input()

    # Split the inputs into lists of values
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a variable to count differences
    difference_count = 0

    # Compare corresponding elements of the two lists
    for index in range(3):  # Adjusted to ensure we only check 3 elements
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
    doMain()
