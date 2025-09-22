def main():
    # Accept two lines of input from the user
    first_input = input()
    second_input = input()

    # Split each input string into a list of numbers
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the numbers are different
        if first_number != second_number:
            # Increment the difference counter
            difference_count += 1 

    # Determine how many differences were found
    if difference_count < 3:
        # If fewer than three differences, print "YES"
        print("YES")
    else:
        # If three or more differences, print "NO"
        print("NO")

# Start the program by calling the main function
main()
