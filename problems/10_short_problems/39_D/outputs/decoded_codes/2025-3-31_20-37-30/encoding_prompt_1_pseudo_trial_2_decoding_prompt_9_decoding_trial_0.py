def main():
    # Read two lines of input
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count differences
    difference_count = 0 
    
    # Loop through the first three positions of both lists
    for index in range(3):
        # Convert the current elements of each list to integers
        number_from_first_list = int(first_list[index])
        number_from_second_list = int(second_list[index])
        
        # Check if the numbers at the current position are different
        if number_from_first_list != number_from_second_list:
            # Increment the difference counter
            difference_count += 1 
    
    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
