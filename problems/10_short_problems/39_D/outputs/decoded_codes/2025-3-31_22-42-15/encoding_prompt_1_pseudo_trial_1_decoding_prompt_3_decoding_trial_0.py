def main():
    # Read two lines of input from the user consecutively
    first_input = input()
    second_input = input()

    # Split the input strings into lists of numbers
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Iterate over the range of the first three elements
    for index in range(3):
        # Convert the corresponding elements from the lists to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # If the numbers at this index are not equal, increment the difference counter
        if first_value != second_value:
            difference_count += 1

    # Check how many differences were found and print the appropriate message
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is being run as the main program
if __name__ == "__main__":
    main()
