def main():
    # Read input from the user
    first_input = input()
    second_input = input()

    # Split input strings into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Check the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Compare elements and count differences
        if first_value != second_value:
            difference_count += 1

    # Determine result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
