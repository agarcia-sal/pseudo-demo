def main():
    # Prompt the user for input
    first_input = input()
    second_input = input()

    # Split the inputs into lists of numbers
    first_numbers = first_input.split()
    second_numbers = second_input.split()

    # Initialize a variable to count differences
    difference_count = 0

    # Compare the numbers at each position
    for index in range(3):
        # Convert to integers for comparison
        first_number = int(first_numbers[index])
        second_number = int(second_numbers[index])

        # If the numbers differ, increment the difference count
        if first_number != second_number:
            difference_count += 1

    # Determine the result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
