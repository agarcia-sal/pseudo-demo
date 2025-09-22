def do_main():
    # Read inputs from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of words
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Compare the two values
        if first_value != second_value:
            # Increment the difference counter if the values are different
            difference_count += 1
    
    # Decide the final output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
do_main()
