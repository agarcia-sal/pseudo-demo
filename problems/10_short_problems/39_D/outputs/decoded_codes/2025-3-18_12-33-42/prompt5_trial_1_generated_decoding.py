def main():
    # Get the first set of three numbers from user input
    first_input = input()
    # Get the second set of three numbers from user input
    second_input = input()

    # Split the input strings into lists of numbers
    first_numbers = first_input.split()
    second_numbers = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare the corresponding numbers from both lists
    for index in range(3):
        # Convert the numbers from string to integer for comparison
        number_from_first = int(first_numbers[index])
        number_from_second = int(second_numbers[index])

        # If the numbers are different, increment the difference counter
        if number_from_first != number_from_second:
            difference_count += 1 

    # Evaluate the total number of differences
    if difference_count < 3:
        # If they differ in fewer than 3 positions, print "YES"
        print("YES")
    else:
        # If they differ in 3 or more positions, print "NO"
        print("NO")

# Start the program by calling the main function
main()
