def do_main():
    # Read two lines of input
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count the differences
    difference_count = 0
    
    # Iterate through the first three elements of both lists
    for index in range(3):  # Assumes there are at least 3 elements in both lists
        # Convert the string values to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Compare the two values
        if first_value != second_value:
            # Increment the count of differences
            difference_count += 1
            
    # Evaluate the number of differences
    if difference_count < 3:
        # Print "YES" if differences are fewer than three
        print("YES")
    else:
        # Print "NO" if differences are three or more
        print("NO")

# Execute the main function when the program starts
do_main()
