def main():
    # Get input from the user
    first_input = input()
    second_input = input()

    # Split the inputs into lists of values
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three items in both lists
    for index in range(3):  # Iterates over indices 0, 1, 2
        # Convert the current items to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Check if the current values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1 

    # Check how many values are different and decide outcome
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
