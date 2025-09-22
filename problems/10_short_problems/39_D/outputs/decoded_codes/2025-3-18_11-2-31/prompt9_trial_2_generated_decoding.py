def main():
    # Get user input for both sets of numbers
    first_input = input()
    second_input = input()

    # Split the inputs into lists of strings for processing
    list_of_first_numbers = first_input.split()
    list_of_second_numbers = second_input.split()

    # Initialize a difference counter
    difference_count = 0

    # Compare corresponding numbers in both lists
    for index in range(3):
        # Convert strings to integers
        number_a = int(list_of_first_numbers[index])
        number_b = int(list_of_second_numbers[index])

        # Increase count if numbers differ
        if number_a != number_b:
            difference_count += 1

    # Check if the number of differences is less than three
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
