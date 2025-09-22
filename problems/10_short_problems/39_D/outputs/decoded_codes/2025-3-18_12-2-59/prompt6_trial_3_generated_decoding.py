def main():
    # Read two lines of input with integer values
    first_input = input()  # Input from the first line
    second_input = input()  # Input from the second line

    # Split the input strings into lists of strings
    first_list = first_input.split()  # List of strings from the first input
    second_list = second_input.split()  # List of strings from the second input

    # Initialize a counter for differing elements
    difference_count = 0  # Counter for differences

    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the current elements of both lists from strings to integers
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Check if the current elements from both lists are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1

    # Determine if the count of differences is less than 3
    if difference_count < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" otherwise

# Start the program by calling the main function
main()
