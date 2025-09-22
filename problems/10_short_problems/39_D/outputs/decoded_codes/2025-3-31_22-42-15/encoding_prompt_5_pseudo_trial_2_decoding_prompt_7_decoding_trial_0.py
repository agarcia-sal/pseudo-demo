def main():
    # Get the first set of numbers from user input
    first_input = input()
    
    # Get the second set of numbers from user input
    second_input = input()
    
    # Split the input strings into lists of numbers
    first_numbers = first_input.split()
    second_numbers = second_input.split()
    
    # Initialize a variable to count differences
    difference_count = 0 
    
    # Loop through the indices of the numbers (0, 1, 2)
    for index in range(3):  # Iterate over the first three indices
        # Convert the current numbers from strings to integers
        num_from_first_list = int(first_numbers[index])
        num_from_second_list = int(second_numbers[index])
        
        # Check if the numbers are different
        if num_from_first_list != num_from_second_list:
            # Increment the count of differences
            difference_count += 1
    
    # Determine the output based on the count of differences
    if difference_count < 3:
        print("YES")  # There are fewer than three differences
    else:
        print("NO")   # There are three or more differences

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
