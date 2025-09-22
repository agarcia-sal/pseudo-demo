def main_procedure():
    # Get two strings as input
    first_input = input()
    second_input = input()

    # Split the input strings into lists based on spaces
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize difference count to zero
    difference_count = 0

    # Compare each element in the lists
    for index in range(3):  # Iterate from 0 to 2
        # Convert the current elements to integers
        first_element = int(first_list[index])
        second_element = int(second_list[index])

        # Check if the elements are different
        if first_element != second_element:
            difference_count += 1  # Increment difference count

    # Check the number of differences
    if difference_count < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" otherwise

# Execute the main_procedure function
main_procedure()
