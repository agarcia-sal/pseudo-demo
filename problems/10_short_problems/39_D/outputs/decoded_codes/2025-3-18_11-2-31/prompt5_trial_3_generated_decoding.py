def main():
    # Accept two lines of input from the user, each containing three numbers
    first_line = input()
    second_line = input()

    # Split the input lines into lists of strings
    list_of_first_numbers = first_line.split()
    list_of_second_numbers = second_line.split()
    
    # Initialize a variable to count the number of differing positions
    difference_count = 0

    # Loop through the indices from 0 to 2 (for three numbers)
    for index in range(3):
        # Convert the current number from each input into an integer
        first_number = int(list_of_first_numbers[index])
        second_number = int(list_of_second_numbers[index])

        # Check if the numbers from both inputs are different
        if first_number != second_number:
            # Increment the count of differences
            difference_count += 1

    # After the loop, check how many positions are different
    if difference_count < 3:
        print("YES")  # There are fewer than three differences
    else:
        print("NO")   # There are three or more differences

# Start the program by calling the main function
main()
