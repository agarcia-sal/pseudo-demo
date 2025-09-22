def main():
    # Read input from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of string representations of numbers
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter to track differences
    difference_count = 0

    # Loop through the first three values of both lists
    for index in range(3): 
        # Convert string values to integers
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])

        # Check if the values are different
        if value_from_first_list != value_from_second_list:
            # Increment the difference counter
            difference_count += 1

    # Check the number of differences and output the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    main()
