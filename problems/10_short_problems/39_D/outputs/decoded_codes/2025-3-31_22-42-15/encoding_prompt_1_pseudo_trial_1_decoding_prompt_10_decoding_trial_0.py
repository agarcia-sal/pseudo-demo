def main():
    # Read two lines of input, each containing a sequence of numbers
    first_input = input()
    second_input = input()

    # Split the input strings into lists of numbers
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Iterate over the range of the first three elements
    for index in range(3):  # Assumes both lists have at least 3 elements
        first_value = int(first_list[index])  # Convert the corresponding elements to integers
        second_value = int(second_list[index])  # Convert the corresponding elements to integers

        # Check if the numbers at this index are not equal
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1

    # After completing the comparisons, check how many differences were found
    if difference_count < 3:
        # Print "YES" if there are fewer than 3 differences
        print("YES")
    else:
        # Print "NO" if there are 3 or more differences
        print("NO")

# Execute the main function if this script is being run as the main program
if __name__ == "__main__":
    main()
