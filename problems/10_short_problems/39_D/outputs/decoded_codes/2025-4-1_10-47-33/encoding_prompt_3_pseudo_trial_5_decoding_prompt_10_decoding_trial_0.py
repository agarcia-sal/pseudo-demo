def do_main():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of components
    components_from_first_input = first_input.split()
    components_from_second_input = second_input.split()
    
    # Initialize a variable to count the number of differences
    difference_count = 0 
    
    # Loop through the first three items of both lists
    for index in range(3):
        # Convert the components at the current index from string to integer
        value_from_first_input = int(components_from_first_input[index])
        value_from_second_input = int(components_from_second_input[index])
        
        # Check if the values are different
        if value_from_first_input != value_from_second_input:
            # Increment the difference counter
            difference_count += 1
    
    # After checking all components, determine if the result is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start of the program execution
if __name__ == "__main__":
    do_main()
