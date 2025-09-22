def main():
    # Read input for two sets of numbers
    first_input = input()
    second_input = input()

    # Split the input strings into lists of numbers
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare the first three numbers in both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the current elements to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # Check if the numbers are different
        if first_number != second_number:
            # Increment the differences counter
            difference_count += 1

    # Determine output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point for the program
if __name__ == "__main__":
    main()
