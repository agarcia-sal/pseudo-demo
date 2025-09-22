def main_procedure():
    # Read the first list of integers as a string
    first_input = input()

    # Read the second list of integers as a string
    second_input = input()

    # Split the input strings into lists of integers
    first_list = list(map(int, first_input.split()))
    second_list = list(map(int, second_input.split()))

    # Initialize a counter for differences
    difference_count = 0 

    # Compare the integers in the two lists
    for index in range(3):
        first_value = first_list[index]
        second_value = second_list[index]

        # If the values differ, increase the difference count
        if first_value != second_value:
            difference_count += 1

    # Check the count of differences to determine the output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main procedure
main_procedure()
