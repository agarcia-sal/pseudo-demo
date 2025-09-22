def do_main():
    # Declare variables
    first_input = ""  # String to hold the first line of input
    second_input = ""  # String to hold the second line of input
    first_list = []  # List to hold the split first input
    second_list = []  # List to hold the split second input
    result_counter = 0  # Integer to count the number of differences
    
    # Get inputs from user
    first_input = input()
    second_input = input()
    
    # Split input strings into lists
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Loop through the first 3 elements of both input lists
    for index in range(3):
        # Convert elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Compare elements and update result counter
        if first_value != second_value:
            result_counter += 1  # Increment the counter
    
    # Check result to determine output
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
do_main()
