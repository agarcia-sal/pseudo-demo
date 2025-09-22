def compare_three_inputs():
    # Prompt user for the first input
    first_input = input()
    
    # Prompt user for the second input
    second_input = input()
    
    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a difference counter
    difference_count = 0
    
    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the current elements from string to integer
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if there's a difference between the two numbers
        if first_number != second_number:
            # Increment difference count if there's a difference
            difference_count += 1
            
    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if program is run directly
if __name__ == "__main__":
    compare_three_inputs()
