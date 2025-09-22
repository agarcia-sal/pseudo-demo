def main_function():
    # Prompt the user for input
    first_input = input()
    second_input = input()

    # Split the input strings into lists of substrings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare corresponding elements in the two lists
    for index in range(3):  # Assuming both lists have at least 3 elements
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Check if the values differ
        if first_value != second_value:
            difference_count += 1 

    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Initiates the main_function when the script is executed
if __name__ == "__main__":
    main_function()
