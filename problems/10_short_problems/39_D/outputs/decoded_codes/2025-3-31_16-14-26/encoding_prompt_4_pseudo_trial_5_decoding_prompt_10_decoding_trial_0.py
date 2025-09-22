def do_main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()

    # Initialize a counter for the differences
    difference_count = 0 
    
    # Loop through the first 3 elements of both lists
    for index in range(3):
        # Convert string elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Compare the two values
        if first_value != second_value:
            # Increment the difference count if they are not the same
            difference_count += 1

    # Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")


# Main execution starts here
if __name__ == "__main__":
    do_main()
