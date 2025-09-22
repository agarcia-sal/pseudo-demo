def main_procedure():
    # Get two strings as input from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists based on spaces
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for the differences
    difference_count = 0

    # Compare each element in the lists
    for index in range(3):
        # Convert the current elements to integers
        first_element = int(first_list[index])
        second_element = int(second_list[index])

        # Check if the elements are different
        if first_element != second_element:
            difference_count += 1

    # Check the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main_procedure function
main_procedure()
