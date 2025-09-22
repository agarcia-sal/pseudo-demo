def main():
    # Get two input strings representing numerical values
    first_set = input()
    second_set = input()

    # Split the input strings into lists of numerical strings
    numbers_from_first_set = first_set.split()
    numbers_from_second_set = second_set.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the range of three positions
    for position in range(3):
        # Convert the current positions' values from strings to integers
        value_from_first_set = int(numbers_from_first_set[position])
        value_from_second_set = int(numbers_from_second_set[position])

        # Check if the values from both sets differ
        if value_from_first_set != value_from_second_set:
            # Increment the difference counter
            difference_count += 1

    # Check the total differences and decide the output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()
