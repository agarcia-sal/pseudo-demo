def main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of each list
    for index in range(3):
        # Convert the current elements to integers
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])
        
        # Check if the two values are different
        if value_from_first_list != value_from_second_list:
            # If they are different, increase the difference counter
            difference_count += 1
    
    # Evaluate the count of differences to decide the output
    if difference_count < 3:
        print("YES")  # The two inputs are similar enough
    else:
        print("NO")   # The two inputs differ too much

# Start the program by calling the main function
main()
