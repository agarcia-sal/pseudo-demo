def main_procedure():
    # Read two input strings
    first_input = input()
    second_input = input()

    # Split the input strings into lists of numbers
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements of both lists to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # Check if the elements are different
        if first_number != second_number:
            difference_count += 1

    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")  # Indicate that there are fewer than 3 differences
    else:
        print("NO")   # Indicate that there are 3 or more differences

# Execute the main procedure
main_procedure()
