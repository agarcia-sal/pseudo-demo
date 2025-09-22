def main():
    # Prompt for user input
    first_input = input()
    second_input = input()

    # Process the inputs
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter
    difference_count = 0

    # Compare the elements of both lists
    for index in range(3):  # We know we will be comparing the first 3 elements
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        if first_value != second_value:
            difference_count += 1

    # Decide the result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Check if this file is executed as the main program
if __name__ == "__main__":
    main()
