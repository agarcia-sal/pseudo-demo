def main():
    # Get two input strings representing numerical values
    first_set = input()  # Input for the first set of numbers
    second_set = input()  # Input for the second set of numbers

    # Split the input strings into lists of numbers
    first_numbers = first_set.split()  # Create a list of numbers from firstSet
    second_numbers = second_set.split()  # Create a list of numbers from secondSet

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the range of three positions
    for position in range(3):
        # Convert the current positions' values from strings to integers
        value_from_first_set = int(first_numbers[position])  # Convert first set number to integer
        value_from_second_set = int(second_numbers[position])  # Convert second set number to integer

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
