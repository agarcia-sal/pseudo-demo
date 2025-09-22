def main():
    # Read two lines of input representing two sets of values
    first_input = input()  # User input for the first set of values
    second_input = input()  # User input for the second set of values

    # Split the input strings into lists of values
    first_values = first_input.split()  # Split first input into a list
    second_values = second_input.split()  # Split second input into a list

    # Initialize a counter for differences
    difference_count = 0

    # Iterate through the first three values of both lists
    for index in range(3):
        # Convert the current values from strings to integers
        value_a = int(first_values[index])
        value_b = int(second_values[index])

        # Compare the current values
        if value_a != value_b:
            # Increment the difference counter if they are different
            difference_count += 1

    # Check the number of differences
    if difference_count < 3:
        print("YES")  # Print YES if fewer than 3 differences
    else:
        print("NO")  # Print NO if 3 or more differences

# Invoke the main function when the script is executed
if __name__ == "__main__":
    main()
