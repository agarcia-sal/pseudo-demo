def main():
    # Get input from the user for the first and second sets of numbers
    first_set_of_numbers = input()
    second_set_of_numbers = input()

    # Split the input strings into lists of individual numbers
    list_of_first_set = first_set_of_numbers.split()
    list_of_second_set = second_set_of_numbers.split()

    # Initialize a counter for the differences
    difference_count = 0

    # Loop through the first three numbers from both sets
    for index in range(3):
        # Convert the current numbers to integers for comparison
        first_number = int(list_of_first_set[index])
        second_number = int(list_of_second_set[index])

        # Check if the numbers are not equal
        if first_number != second_number:
            # Increment the counter if there is a difference
            difference_count += 1

    # Determine if the number of differences is less than three
    if difference_count < 3:
        print("YES")  # The sets are similar enough
    else:
        print("NO")   # The sets differ too much

# Main execution starts here
main()
