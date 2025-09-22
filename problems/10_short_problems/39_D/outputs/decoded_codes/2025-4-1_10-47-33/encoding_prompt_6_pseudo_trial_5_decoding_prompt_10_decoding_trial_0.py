def main():
    # Read two lines of input, each containing three numbers separated by spaces
    first_line = input()
    second_line = input()

    # Split the input lines into lists of strings, representing the numbers
    first_list = first_line.split()
    second_list = second_line.split()

    # Initialize a counter for the number of differences
    difference_count = 0 

    # Loop through the first three elements of each list
    for index in range(3):
        # Convert the string numbers to integers
        num_from_first_list = int(first_list[index])
        num_from_second_list = int(second_list[index])

        # Check if the numbers at the current index are different
        if num_from_first_list != num_from_second_list:
            # Increment the difference counter
            difference_count += 1 

    # If the count of differences is less than 3, print "YES", otherwise print "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
