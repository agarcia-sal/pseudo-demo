def main():
    # Prompt the user for two inputs
    first_input = input()
    second_input = input()

    # Split the inputs into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Compare the elements of both lists
    for index in range(3):
        # Convert string elements to integers for comparison
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])

        # Check if the values are different
        if value_from_first_list != value_from_second_list:
            difference_count += 1

    # Evaluate how many differences were found
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
