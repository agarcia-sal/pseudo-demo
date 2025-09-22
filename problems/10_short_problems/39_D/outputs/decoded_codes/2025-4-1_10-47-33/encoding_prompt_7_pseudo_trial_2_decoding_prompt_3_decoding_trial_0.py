def do_main():
    # Read the two inputs from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differing elements
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the elements are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1 

    # Determine output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    do_main()
