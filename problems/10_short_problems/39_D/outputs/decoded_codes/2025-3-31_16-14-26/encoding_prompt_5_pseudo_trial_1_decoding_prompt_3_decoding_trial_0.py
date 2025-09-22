def main():
    # Get input from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of numbers
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize the difference counter
    difference_count = 0 

    # Loop through the first three elements of both lists and compare them
    for index in range(3):
        # Convert the corresponding elements to integers for comparison
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        # If the numbers are not equal, increase the difference counter
        if first_number != second_number:
            difference_count += 1
            
    # Check the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
