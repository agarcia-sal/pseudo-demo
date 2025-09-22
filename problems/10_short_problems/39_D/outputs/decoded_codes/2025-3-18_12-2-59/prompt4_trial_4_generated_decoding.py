def doMain():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()

    # Split the inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Iterate over the first three elements of the lists
    for index in range(3):
        # Convert the elements to integers
        value_a = int(first_list[index])
        value_b = int(second_list[index])

        # Compare the two values
        if value_a != value_b:
            difference_count += 1 

    # Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the script is run
if __name__ == "__main__":
    doMain()
