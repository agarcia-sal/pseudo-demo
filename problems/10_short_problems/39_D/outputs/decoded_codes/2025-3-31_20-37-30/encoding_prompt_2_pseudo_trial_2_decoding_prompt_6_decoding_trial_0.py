# Start the program
def do_main():
    # Get user input
    first_input = input()  # Read the first input line
    second_input = input()  # Read the second input line

    # Split the inputs into lists
    first_list = first_input.split()  # Split first input by spaces
    second_list = second_input.split()  # Split second input by spaces

    # Initialize a counter
    difference_count = 0  # Track how many elements differ between the two lists

    # Compare corresponding elements from the two lists
    for index in range(3):  # Loop through indices from 0 to 2
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        if first_value != second_value:  # Check for differences
            difference_count += 1  # Increase counter if values differ

    # Determine the result based on the count of differences
    if difference_count < 3:  
        print("YES")  # Print "YES" if less than 3 differences
    else:
        print("NO")   # Print "NO" otherwise

# Execute the main function if the program is run as the main module
if __name__ == "__main__":
    do_main()
