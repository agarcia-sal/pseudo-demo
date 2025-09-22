def do_main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    number_list1 = first_line.split()
    number_list2 = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from string to integer
        value1 = int(number_list1[index])
        value2 = int(number_list2[index])
        
        # If the values are not equal, increment the difference counter
        if value1 != value2:
            difference_count += 1

    # Check the total number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
