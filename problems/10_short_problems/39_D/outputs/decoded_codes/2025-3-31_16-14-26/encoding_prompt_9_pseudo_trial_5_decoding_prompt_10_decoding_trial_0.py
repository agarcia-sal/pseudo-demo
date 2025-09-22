def do_main():
    # Receive first input
    first_input = input()
    # Receive second input
    second_input = input()

    # Split inputs into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the range from 0 to 2 (for three comparisons)
    for i in range(3):
        # Convert the elements at index i to integers
        value_from_first = int(first_list[i])
        value_from_second = int(second_list[i])
        
        # Check if the two values are not equal
        if value_from_first != value_from_second:
            difference_count += 1

    # Check the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the function do_main when the program starts
if __name__ == "__main__":
    do_main()
