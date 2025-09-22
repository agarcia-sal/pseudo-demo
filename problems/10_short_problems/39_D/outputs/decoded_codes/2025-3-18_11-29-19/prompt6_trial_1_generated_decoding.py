def main():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()

    # Split the input lines into individual strings
    first_input_parts = first_input.split()
    second_input_parts = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of both input lists
    for index in range(3):  # We're only interested in the first three elements
        # Convert the string elements to integers
        first_value = int(first_input_parts[index])
        second_value = int(second_input_parts[index])

        # Check if the values at the current index are different
        if first_value != second_value:
            # Increment the count of differences
            difference_count += 1

    # Check how many differences were counted
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
