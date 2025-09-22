def do_main():
    # Initialize variables
    result_counter = 0
    
    # Get inputs from the user
    first_input = input()
    second_input = input()
    
    # Split input strings into lists
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Loop through the first three elements of both input lists
    for index in range(3):
        try:
            # Convert string elements to integers
            first_number = int(first_list[index])
            second_number = int(second_list[index])
            
            # Compare elements and update result counter if they differ
            if first_number != second_number:
                result_counter += 1
        except (IndexError, ValueError):
            # Handle cases where less than three integers are present or conversion fails
            print("Please ensure both inputs contain at least three valid integers.")
            return
    
    # Check result to determine output
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
do_main()
