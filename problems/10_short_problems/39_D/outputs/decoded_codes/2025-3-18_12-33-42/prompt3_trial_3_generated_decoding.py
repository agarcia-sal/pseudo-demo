def main():
    # Read input values from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()

    # Initialize a counter to track the number of differences
    difference_count = 0

    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the current element from both lists to integers
        value_from_first_list = int(first_values[index])
        value_from_second_list = int(second_values[index])

        # Check if the values from the two lists are different
        if value_from_first_list != value_from_second_list:
            difference_count += 1

    # Determine the result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
