# Define the main procedure
def do_main():
    # Read two input strings from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of substrings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differing elements
    difference_count = 0 

    # Iterate over the indices for the lists (assuming they both have 3 elements)
    for index in range(3):  # Loop from 0 to 2 (3 elements)
        # Convert the elements to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # Compare the corresponding elements
        if first_number != second_number:
            # Increment the counter if they are different
            difference_count += 1

    # Check how many elements differ
    if difference_count < 3:
        print("YES")  # Output "YES" if less than 3 differences
    else:
        print("NO")   # Output "NO" if 3 or more differences

# Main execution begins here
if __name__ == "__main__":
    do_main()
