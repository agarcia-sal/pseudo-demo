def main():
    # Read two sets of inputs from the user
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_counter = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])
        
        # Check if the elements are different
        if value_from_first_list != value_from_second_list:
            # Increment the difference counter
            difference_counter += 1 
    
    # Evaluate the number of differences and print the result
    if difference_counter < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":    
    main()
