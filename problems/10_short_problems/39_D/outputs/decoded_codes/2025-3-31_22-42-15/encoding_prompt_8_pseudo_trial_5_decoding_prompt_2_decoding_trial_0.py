def main():
    # Read two lines of input from the user, each representing a set of integers
    first_input = input()
    second_input = input()

    # Split the inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter to keep track of differences
    difference_count = 0 

    # Loop through each index from 0 to 2 (representing the three integers)
    for index in range(3):
        # Convert the string representations to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # Check if the values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1 

    # Determine whether the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run
if __name__ == "__main__":
    main()
