def do_main():
    # Read two lines of input, each containing three space-separated integers
    first_line = input()
    second_line = input()
    
    # Split the input strings into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a variable to count the number of differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from strings to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])

        # If the values are not equal, increment the difference counter
        if first_value != second_value:
            difference_count += 1

    # If the number of differences is less than 3, print "YES"
    if difference_count < 3:
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Execute the main function when this script is run directly
if __name__ == "__main__":
    do_main()


     1 2 3
     1 2 3
     

     1 2 3
     4 2 3
     

     1 2 3
     4 5 6
     

     2 2 3
     2 2 3
     